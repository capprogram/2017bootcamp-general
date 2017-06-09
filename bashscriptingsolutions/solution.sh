#!/bin/bash
# Searches .dat files in $dataDir for lines with field=$1, 
# analyzes these lines using an external python script (./analyze.py),
# and saves the resulting output in a directory named for today's day of the week

dataDir=data/ # directory we take data from (MAKE SURE THIS IS CORRECT!)

# Must receive one command line argument, equal to field value
if [ $# -eq 1 ]; then
  field=$1
else
  echo "Usage: $0 <field value>"
  exit 1
fi

outputFile="field-$field.out" # name of output file that will hold analyzed data

# For each .dat file in $dataDir, pull lines matching field value given by user
for file in ${dataDir}/*.dat; do
  grep "field=$field" $file >> tmpInput.txt
done

if ! grep "field=$field" tmpInput.txt > /dev/null  # make sure something was found (! negates, and we throw away output with /dev/null)
then
  echo "No fields with that value found"
  rm tmpInput.txt
  exit
fi

# Analyzed data will be stored in a directory named with today's day of the week
saveDir=$(date +%A)
mkdir -p $saveDir # -p flag only creates if not already created

# Analyze data in input file and save output as $outputFile (and make sure worked ok)
if ./analyze.py tmpInput.txt $outputFile     
then
  mv $outputFile $saveDir                      # move analysis output to new directory
else
  exit 1                                       # if python script had a problem, exit this script
fi

# Clean up after ourselves
rm tmpInput.txt

