#/bin/bash

export LFC_HOST=lfc.grid.sara.nl

ENVPATH=$1
ENVNAME=`basename $ENVPATH`

#load environment
gcp $ENVPATH .
tar -xzvf $ENVNAME
cd sys_enhance
cat _set_python_env.sh | sed s#ONAME#$TMPDIR#g > set_python_env.sh
source set_python_env.sh

