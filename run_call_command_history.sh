#!/usr/bin/env bash

module load jamo
 made a list of libraries.info
#### for x in $(cat libraries.info); do jamo link library $x ; echo $x ; done

### 1.  get the full path info for each demultiplexed individual and write to a file
find `pwd` | grep "fastq.gz" > finalMappingLibSet.dat
find `pwd` | grep "fastq.gz" > finalMappingLibSet.dat


### 2.  with first lines uncommented in makeSubmissionFiles.py, this generates bunch of .sh files
python /global/homes/s/sgordon/scripts/python/jerry/makeSubmissionFiles_BhybridumBroken_ronan.py

### when thing go wrong, you can kill all submissions:
qdel -u sgordon

### 3.  submit the .sh files
 for x in $(cat finalMappingLibSet.dat | cut -f2 | cut -f7 -d"/" | cut -f1-6 -d"."); do echo $x ; qsub kmers.$x.PNWH.sh ; qsub kmers.$x.UCXX.sh ; done


### need to comment and uncomment the makeSubmissionFiles.py script, then run again:
python /global/homes/s/sgordon/scripts/python/jerry/makeSubmissionFiles_BhybridumBroken_ronan.py


### submit the shell scripts to qsub:
for x in $(cat finalMappingLibSet.dat | cut -f2 | cut -f7 -d"/" | cut -f1-6 -d"."); do echo $x ; qsub calling.$x.sh ; done

### decompress the calling files:
for f in *calling.dat.bz2; do
    bunzip2 "${f}"
done


