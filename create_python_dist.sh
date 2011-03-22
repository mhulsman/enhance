#/bin/bash
set -e

CURDIR=`pwd`
SCRIPTDIR="$(dirname "$(readlink -f ${BASH_SOURCE[0]})")"
DIRNAME=sys_enhance

echo "Creating environment for $ENVNAME"

mkdir src
cd src

wget http://www.bzip.org/1.0.6/bzip2-1.0.6.tar.gz
wget http://www.python.org/ftp/python/2.7/Python-2.7.tgz
wget http://pypi.python.org/packages/source/s/setuptools/setuptools-0.6c11.tar.gz#md5=7df2a529a074f613b509fb44feefe74e
wget http://www.openssl.org/source/openssl-1.0.0a.tar.gz
wget http://pypi.python.org/packages/source/p/pyOpenSSL/pyOpenSSL-0.10.tar.gz#md5=34db8056ec53ce80c7f5fc58bee9f093
wget http://downloads.sourceforge.net/project/numpy/NumPy/1.5.1/numpy-1.5.1.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fnumpy%2Ffiles%2FNumPy%2F1.5.1%2F&ts=1291647102&use_mirror=garr
wget http://downloads.sourceforge.net/project/scipy/scipy/0.8.0/scipy-0.8.0.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fscipy%2F&ts=1287566242&use_mirror=kent
wget ftp://ftp.cwru.edu/pub/bash/readline-6.1.tar.gz
wget http://ftp.gnu.org/pub/gnu/ncurses/ncurses-5.7.tar.gz
wget http://www.sqlite.org/sqlite-amalgamation-3.7.3.tar.gz
wget http://downloads.sourceforge.net/project/math-atlas/Stable/3.8.3/atlas3.8.3.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fmath-atlas%2Ffiles%2F&ts=1288347255&use_mirror=kent
wget http://www.netlib.org/lapack/lapack-3.2.1.tgz
wget http://www.kernel.org/pub/software/scm/git/git-1.7.4.tar.gz

tar -xzf bzip2-1.0.6.tar.gz
cd bzip2-1.0.6
make -f Makefile-libbz2_so
make install PREFIX=$CURDIR/$DIRNAME
cd ..

tar -xzf openssl-1.0.0a.tar.gz
cd openssl-1.0.0a
./config shared --prefix=$CURDIR/$DIRNAME
make
make install
cd ..

tar -xzf lapack-3.2.1.tgz
cd lapack-3.2.1
sed -e "s:OPTS     =:OPTS = -fPIC:g" -e "s:NOOPT    =:NOOPT = -fPIC:g" make.inc.example > make.inc
make blaslib
make
cd ..

tar -xzf atlas3.8.3.tar.gz
cd ATLAS
mkdir build_dir
cd build_dir
../configure -Fa alg -fPIC --with-netlib-lapack=../../lapack-3.2.1/lapack_LINUX.a --prefix=$CURDIR/$DIRNAME
make
make install
cd ..
cd ..


tar -xzf ncurses-5.7.tar.gz 
cd ncurses-5.7
./configure --enable-shared --prefix=$CURDIR/$DIRNAME CFLAGS="-fPIC"
make
make install
cd ..
ln -s $CURDIR/$DIRNAME/include/ncurses/curses.h $CURDIR/$DIRNAME/include/curses.h
ln -s $CURDIR/$DIRNAME/include/ncurses/ncurses.h $CURDIR/$DIRNAME/include/ncurses.h
ln -s $CURDIR/$DIRNAME/include/ncurses/panel.h $CURDIR/$DIRNAME/include/panel.h

tar -xzf readline-6.1.tar.gz 
cd readline-6.1
./configure --prefix=$CURDIR/$DIRNAME
make
make install
cd ..

tar -xzf sqlite-amalgamation-3.7.3.tar.gz 
cd sqlite-3.7.3
./configure --prefix=$CURDIR/$DIRNAME
make
make install
cd ..

tar -xzf Python-2.7.tgz 
cd Python-2.7
./configure --enable-shared --prefix=$CURDIR/$DIRNAME
make
make install
cd ..
cp  $SCRIPTDIR/_set_python_env.sh $CURDIR/$DIRNAME/_set_python_env.sh
cat $CURDIR/$DIRNAME/_set_python_env.sh | sed s#ONAME#$CURDIR#g > set_python_env.sh
source set_python_env.sh
cd Python-2.7
python setup.py install --prefix=$CURDIR/$DIRNAME
cd ..

tar -xzf setuptools-0.6c11.tar.gz
cd setuptools-0.6c11
python setup.py install --prefix=$CURDIR/$DIRNAME
cd ..

tar -xzf pyOpenSSL-0.10.tar.gz
cd pyOpenSSL-0.10
python setup.py build_ext -I$CURDIR/$DIRNAME/include/openssl -L$CURDIR/$DIRNAME/lib
python setup.py install --prefix=$CURDIR/$DIRNAME
cd ..

easy_install foolscap
easy_install twisted
easy_install ipython
#increase max number of engines
sed -i -e "s:511:5511:g" $CURDIR/$DIRNAME/lib/python2.7/site-packages/ipython-0.10.1-py2.7.egg/IPython/kernel/controllerservice.py 


tar -xzf numpy-1.5.1.tar.gz
cd numpy-1.5.1
python setup.py install --prefix=$CURDIR/$DIRNAME
cd ..

tar -xzf scipy-0.8.0.tar.gz
cd scipy-0.8.0
wget http://projects.scipy.org/scipy/raw-attachment/ticket/1180/0001-FIX-define-macro-to-access-C99-extensions-from-C.patch
patch -p1 < 0001-FIX-define-macro-to-access-C99-extensions-from-C.patch
python setup.py install --prefix=$CURDIR/$DIRNAME
cd ..

easy_install zope.app.interface
easy_install sqlalchemy
easy_install psutil
easy_install dnspython

tar -xzvf git-1.7.4.tar.gz
cd git-1.7.4
make NO_EXPAT=YesPlease NO_TCLTK=YesPlease prefix=$CURDIR/$DIRNAME all install
cd ..

git clone https://mhulsman@github.com/mhulsman/cluster_storage.git
cd cluster_storage
python setup.py install --prefix=$CURDIR/$DIRNAME
cd ..

mkdir $CURDIR/$DIRNAME/work
cp $SCRIPTDIR/bin/* $CURDIR/$DIRNAME/bin/

#out of src dir
cd $CURDIR

cp $CURDIR/src/set_python_env.sh .
chmod 744 set_python_env.sh

cp $SCRIPTDIR/upload_env.sh .
chmod 744 upload_env.sh

cp $SCRIPTDIR/load_env.jdl .
cp $SCRIPTDIR/load_env.sh .
cp $SCRIPTDIR/load_env_worker.sh .
cp $CURDIR/$DIRNAME/bin/gcp .
cp $CURDIR/$DIRNAME/bin/greplicate .
cp $CURDIR/$DIRNAME/bin/cluster_storage.py .

