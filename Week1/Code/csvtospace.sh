#!/bin/bash
# Author: Jamal Khan jak112@imperial.ac.uk
# Script: csvtospace.sh
# Desc: substitute the commas in a file with spaces and saves it to a different .sp file
#
# Arguments: 1-> space delimited file
# Date: Oct 2018

echo "Creating a space delimited version of $1 ..."
cat $1 | tr -s "," " "  >> $1.sp
echo "Done!"
exit
