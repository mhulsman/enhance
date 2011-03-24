#/bin/bash
CURDIR=`pwd`
GRIDPATH=$1
ENVNAME=`basename $GRIDPATH`

#create environment archive
tar -czvf $ENVNAME $CURDIR/sys_enhance
./gcp $ENVNAME $GRIDPATH
./greplicate $GRIDPATH

