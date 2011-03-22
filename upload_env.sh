#/bin/bash
ENVPATH=$1
GRIDPATH=$2
ENVNAME=`basename $GRIDPATH`

CURDIR=`pwd`
#create environment archive
tar -czvf $ENVNAME $ENVPATH/sys_enhance
gcp $ENVNAME $GRIDPATH
greplicate $GRIDPATH

