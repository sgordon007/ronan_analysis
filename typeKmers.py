__author__="Jerry Jenkins, jjenkins@hudsonalpha.org"
__date__ ="Created:  7/17/14"

from sys import argv

import subprocess

from os.path import split

from sys import stdout

from string import maketrans

translationTable = maketrans("ATCG", "TAGC")

#==============================================================
def revComp( seq ):
    return seq.translate(translationTable)[::-1]

#==============================================================
def kmerize( oh, merSize ):
    while (True):
        line1 = oh.readline()
        seq   = oh.readline().strip()
        line3 = oh.readline()
        line4 = oh.readline()
        if ( not line4 ): return
        ID = line1[1:].strip().split(' ')[0].split('/')[0]
        for n in xrange( len(seq) - merSize + 1 ):
            kmer = seq[ n : (n+merSize) ]
            yield ID, kmer
            yield ID, revComp( kmer )
        #####
    #####
    return

#==============================================================
def real_main():
    
    # Getting the inputs
    reseqFile     = argv[1]
    kmerFile      = argv[2]
    merSize       = int(argv[3])
    bannedMarkers = argv[4]
    
    # Reading in the banned markers
    bannedSet = set([line.strip() for line in open(bannedMarkers)])
    
    # Reading in the kmers file
    kmerDict    = {}
    counterDict = {}
    keepDict    = {1:None}
    for line in open( kmerFile ):
        if ( line[0] == '>' ):
            keepKmer = 1
            ID = line[1:].strip()
            if ( '|'.join(ID.split('|')[:2]) in bannedSet ): keepKmer = 0
        else:
            try:
                n                 = keepDict[keepKmer]
                kmer              = line.strip()
                kmerDict[kmer]    = ID
                counterDict[kmer] = set()
            except KeyError:
                continue
            #####
        #####
    #####
    
    # Reading in kmers
    p = subprocess.Popen('cat %s | gunzip -c'%reseqFile,shell=True,stdout=subprocess.PIPE)
    for ID, kmer in kmerize( p.stdout, merSize ):
        try:
            counterDict[kmer].add( ID )
        except KeyError:
            pass
        #####
    #####
    p.poll()
    
    # Providing output
    for kmer, tmpSet in counterDict.iteritems():
        if ( len(tmpSet) == 0 ): continue
        stdout.write('%s\t%s\t%s\n'%( kmerDict[kmer],kmer,';'.join(tmpSet)))
    #####

#==============================================================
if ( __name__ == '__main__' ):
    real_main()
