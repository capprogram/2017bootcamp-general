#!/bin/bash
# Prints personal greeting, and checks for proper usage

if [ $# -ne 1 ]
then
  echo "Usage: $0 <yourname>"
  exit 1
else
  echo "Hello ${1}!"
fi
