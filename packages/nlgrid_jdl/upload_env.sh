#!/bin/bash
set -e

####
# Example usage: ./upload_env.sh grid:/choose_a_name.dist
# Note: only call from root path of environment!!!
###
CURDIR=`pwd`
GRIDPATH=$1
ENVNAME=`basename $GRIDPATH`

#create environment archive
echo "Packing environment..."
tar -czvf $ENVNAME ./sys_enhance

echo "Uploading environment..."
./sys_enhance/bin/gcp $ENVNAME $GRIDPATH

echo "Replicating environment..."
./sys_enhance/bin/greplicate $GRIDPATH

