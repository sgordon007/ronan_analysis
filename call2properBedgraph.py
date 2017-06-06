#!/usr/bin/env python

callFiles = [] 
fileList = open('fastq_calling.bed.list.txt', 'r')
for file in fileList:
    file.strip()
    callFiles.append(file)

def call2properBedgraph(callFiles):
    """Takes a list of genotype files with only one column for pos and converts them to proper bedgraph format to be sorted"""
    for callFile in callFiles:
        f = callFile.rstrip()
        print f
        outFileName = f[:f.rfind('.')]+'.bedgraph'
        inputFile = open(f, 'r')
        open(outFileName, 'w').close()
        outputFile = open(outFileName, 'w')
        for line in inputFile:
            lineInList = line.split()
            if lineInList[4] == "UCXX":
                genotype_num = 1
            elif lineInList[4] == "PNWH":
                genotype_num = -1
            elif lineInList[4] == "HET":
                genotype_num = 0.1
            elif lineInList[4] == "UNK":
                continue
            lineOutputList = [lineInList[0], int(lineInList[1]), int(lineInList[1])+1, lineInList[3], genotype_num]
            outputFile.write('%s\t%d\t%d\t%s\t%d\n' % tuple(lineOutputList))
        inputFile.close()
        outputFile.close()

call2properBedgraph(callFiles)