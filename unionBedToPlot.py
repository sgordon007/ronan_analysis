__author__ = 'sgordon007'

import pybedtools
import sys

callFiles = []
fileList = open('fastq_calling.bed.list.txt', 'r')
for file in fileList:
    file.strip()
    callFiles.append(file)

def BedgraphToUnion(callFiles):
    """Takes a list of genotype files with only one column for pos and converts them to proper bedgraph format to be sorted"""
    for callFile in callFiles:
        f = callFile.rstrip()
        input_new = f[:f.rfind('.')]+'.bedgraph'
        a = pybedtools.BedTool(input_new).sort()
        outFileName = f[:f.rfind('.')]+'.sorted.bedgraph'
        print 'creating:' + outFileName
        a.saveas(outFileName)

def bed_union(a=str(sys.argv[1]), b=str(sys.argv[2]), c=str(sys.argv[3])):
    pref1 = a[:a.lfind('.')]
    pref2 = b[:b.lfind('.')]
    pref3 = c[:c.lfind('.')]
    outFileName = pref1 + '.' + pref2 + '.' + pref3 + '.' +'.union.bedgraph'
    x = pybedtools.BedTool()
    result = x.union_bedgraphs(i=[a.fn, b.fn, c.fn], g="GENE_LENGTH_Brachypodium_hybridum.mainGenome.scaffolds.gapfilled.091816.fasta")
    print result
    result.saveas(outFileName)

if __name__ == "__main__":
    # BedgraphToUnion(callFiles)
    bed_union(a=str(sys.argv[1]), b=str(sys.argv[2]), c=str(sys.argv[3]))


#
# BedgraphToUnion(int(sys.argv[1]))
