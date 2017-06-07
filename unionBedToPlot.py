__author__ = 'sgordon007'

import pybedtools


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
        # print input_new
        a = pybedtools.BedTool(input_new).sort()
        outFileName = f[:f.rfind('.')]+'.sorted.bedgraph'
        # print outFileName
        a.saveas(outFileName)

"""
        open(outFileName, 'w').close()
        outputFile = open(outFileName, 'w')


a = pybedtools.BedTool('BTNCA.11436.8.207067.ACTCGCT-TATCCTC.fastq_calling.bedgraph')
b = pybedtools.BedTool('BTNCX.11436.8.207067.GGAGCTA-CGTCTAA.fastq_calling.bedgraph')
c = pybedtools.BedTool('BTNGT.11436.8.207067.CGGAGCC-GTAAGGA.fastq_calling.bedgraph')
#print (a).count()

        outputFile.write(a.sort())
        outputFile.write(a.sort())
        outputFile.write(a.sort())
inputFile.close()
outputFile.close()
"""

"""
print a.sort()
print b.sort()
print c.sort()
"""


#aS = a.sort()
"""
bS = b.sort()
cS = c.sort()
"""

if __name__ == "__main__":
    BedgraphToUnion(callFiles)

# import sys
# BedgraphToUnion(int(sys.argv[1]))


#print aS

#x = pybedtools.BedTool()
#>>> a = pybedtools.example_bedtool('a.bed')
#>>> b = pybedtools.example_bedtool('b.bed')
#result = x.union_bedgraphs(i=[aS.fn, bS.fn, cS.fn], g="GENE_LENGTH_Brachypodium_hybridum.mainGenome.scaffolds.gapfilled.091816.fasta")
#print result


#call2properBedgraph(callFiles)


#bedAnalyze = BedTool('%s.bed'%(syntenicInputFiles[0][:syntenicInputFiles[0].rfind('.')])).sort()

    # old debug method...
    #stop=1 #pause here and drag bed file to new location

    ###########
    #return bedAnalyze # this is our BedTool object

#u = [a,b,c]
#print u
#uBG = pybedtools.bedtool.BedTool.union_bedgraphs(a)
