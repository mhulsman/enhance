#/bin/bash
set -e

export LFC_HOST=lfc.grid.sara.nl

ENVPATH=$1
ENVNAME=`basename $ENVPATH`

#load environment
echo "Downloading environment"
gcp $ENVPATH .

echo "Unpacking environment"
tar -xzvf $ENVNAME

CURDIR=`pwd`

cd sys_enhance
cat _paths | sed s#ONAME#$CURDIR#g > paths

echo "Done. Use 'source paths' to enter."
