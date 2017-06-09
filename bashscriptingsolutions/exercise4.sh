#!/bin/bash
# Prepends 'test' to the beginning of .dat files

if [ $# -eq 1 ]; then
  cd $1
elif [ $# -gt 1 ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

for file in *.dat
do
  mv "$file" "test$file"  # Note the double quotes, in case a filename has spaces
done
  
