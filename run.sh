#!/bin/bash

if [[ $# -lt 1 ]] ; then
  echo "ERROR: No file selected!"
  exit 0
else
  FILENAME=$1
  shift
fi

tshark -r $FILENAME -T fields -E separator=, -e ip.src -e ip.dst > $FILENAME.txt

python3 main.py -f $FILENAME.txt