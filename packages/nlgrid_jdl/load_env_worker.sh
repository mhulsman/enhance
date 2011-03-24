#/bin/bash

ENVPATH=$1
PARAMNR=$2
ENVNAME=`basename $ENVPATH`

export LFC_HOST=lfc.grid.sara.nl

#Wait a random time to not overload the server after submission of a number of jobs.
echo "Waiting..."
WAIT=$[ ($RANDOM % 180) ]
sleep $WAIT
echo "Waiting period over for $PARAMNR, starting bootstrap."

#load environment
chmod 744 ./gcp
./gcp $ENVPATH .
tar -xzf $ENVNAME
CURDIR=`pwd`
cd sys_enhance
cat _set_python_env.sh | sed s#ONAME#$CURDIR#g > set_python_env.sh
source set_python_env.sh
echo "Environment loaded for $PARAMNR, starting work."

#run job
cd work
########################################################################
# Put your scripts in directory work                                   #
# Call them from here                                                  #
########################################################################


#cleaning
echo "Work for $PARAMNR finished, cleaning up..."
cd /
rm -rf $CURDIR/sys_enhance
echo "Done"

