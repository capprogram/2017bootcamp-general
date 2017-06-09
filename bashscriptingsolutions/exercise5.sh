#!/bin/bash
# Reports whether a file, prompted from the user, is in the current directory

file=""
while [ "$file" != "stop" ]
do
  echo "Gimme a file:"
  read file
  if [ -e "$file" ]
  then
    echo "Yep, $file is here"
  else
    echo "Nope, $file is not here"
  fi
done
