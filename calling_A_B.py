__author__ = "Jerry Jenkins, jjenkins@hudsonalpha.org"
__date__   = "Created:  7/10/14"

from os.path import split

from sys import argv, stdout

import subprocess

#==============================================================
class locationClass(object):
    def __init__(self,scaffID,pos,A_key,B_key):
        self.scaffID = scaffID
        self.pos     = int(pos)

        self.A_key   = A_key
        self.A_kmer  = None
        self.A_counter = 0

        self.B_key   = B_key
        self.B_kmer  = None
        self.B_counter  = 0

    def add_A_kmer(self,kmer):
        self.A_kmer = kmer
    
    def add_B_kmer(self,kmer):
        self.B_kmer = kmer

    def isA(self,nReads):
        self.A_counter += nReads
    
    def isB(self,nReads):
        self.B_counter += nReads

### this was for haploid genome and ignore HETs:
    #def generateOutputString(self):
    #    # Prepping the outputList
    #    outputList = [self.scaffID]
    #    outputList.append( '%d'%self.pos )
    #    outputList.append( self.A_kmer )
    #    outputList.append( self.B_kmer )
    #    # Computing the type
    #    if ( self.A_counter > self.B_counter ): 
    #        outputList.append( self.A_key )
    #    elif ( self.B_counter > self.A_counter ): 
    #        outputList.append( self.B_key )
    #    else:
    #        outputList.append( 'UNK' )
    #    #####
    #    outputList.append( '%s=%d'%(self.A_key,self.A_counter) )
    #    outputList.append( '%s=%d'%(self.B_key,self.B_counter) )
    #    return '\t'.join( outputList )
    

### this is for diploid genome and outputs HETs:    
    def generateOutputString(self):
        # Prepping the outputList
        outputList = [self.scaffID]
        outputList.append( '%d'%self.pos )
        outputList.append( self.A_kmer )
        outputList.append( self.B_kmer )
        # Computing the type
        if ( (self.A_counter >= 1) or (self.B_counter >= 1) ):
            if ( self.A_counter >= 1 ):
                if ( self.B_counter >= 1 ):
                    outputList.append( 'HET' )
                else:
                    if ( self.A_counter >= 1 ):
                        outputList.append( self.A_key )
                    else:
                        outputList.append( 'UNK' )
                    #####
                #####
            else:
                if ( self.B_counter >= 1 ):
                    outputList.append( self.B_key )
                else:
                    outputList.append( 'UNK' )
                #####
            #####
        else:
            outputList.append( 'UNK' )
        #####
    
        outputList.append( '%s=%d'%(self.A_key,self.A_counter) )
        outputList.append( '%s=%d'%(self.B_key,self.B_counter) )
    
        return '\t'.join( outputList )


#==============================================================
def real_main():

    # Reading in the inputs
    fileBase = argv[1]

    A_key    = argv[2]
    A_kmers  = argv[3]

    B_key    = argv[4]
    B_kmers  = argv[5]
    
    mainPath      = argv[6]
    bannedMarkers = argv[7]
    
    # Reading in the banned markers
    bannedSet = set([line.strip() for line in open(bannedMarkers)])
    
    # Main dictionary
    mainDict  = {}
    sepString = "===========================\n"
    
    # Reading in the "A" kmers
    print "%s kmers"%A_key
    for line in open( A_kmers ):
        if ( line[0] == '>' ):
            scaffID, pos, tmpType = line.strip()[1:].split('|')
            posID                 = "%s|%s"%(scaffID,pos)
            if ( posID in bannedSet ): continue
            mainDict[posID]       = locationClass(scaffID,pos,A_key,B_key)
        else:
            if ( posID in bannedSet ): continue
            kmer = line.strip()
            mainDict[posID].add_A_kmer( kmer )
        #####
    #####
    
    # Reading in the "B" kmers
    print "%s kmers"%B_key
    for line in open( B_kmers ):
        if ( line[0] == '>' ):
            scaffID, pos, tmpType = line.strip()[1:].split('|')
            posID                 = "%s|%s"%(scaffID,pos)
            if ( posID in bannedSet ): continue
        else:
            if ( posID in bannedSet ): continue
            kmer = line.strip()
            mainDict[posID].add_B_kmer( kmer )
        #####
    #####
    
    # Analyzing the A file
    print '%s calling file'%A_key
    print '%s/%s.%s.dat.bz2'%(mainPath,fileBase,A_key)
    p = subprocess.Popen( 'cat %s/%s.%s.dat.bz2 | bunzip2 -c'%(mainPath,fileBase,A_key), shell=True, stdout=subprocess.PIPE )
    nSNPS_A = 0
    for line in p.stdout:
        ID, seq, reads        = line.split(None)
        nReads                = len( set( [item for item in reads.split(';')] ) )
        scaffID, pos, tmpType = ID.split('|')
        posID                 = "%s|%s"%(scaffID,pos)
        mainDict[posID].isA(nReads)
        nSNPS_A += 1
    #####
    p.poll()

    # Analyzing the B file
    print '%s calling file'%B_key
    print '%s/%s.%s.dat.bz2'%(mainPath,fileBase,B_key)
    p = subprocess.Popen( 'cat %s/%s.%s.dat.bz2 | bunzip2 -c'%(mainPath,fileBase,B_key), shell=True, stdout=subprocess.PIPE )
    nSNPS_B = 0
    for line in p.stdout:
        ID, seq, reads        = line.split(None)
        nReads                = len( set( [item for item in reads.split(';')] ) )
        scaffID, pos, tmpType = ID.split('|')
        posID                 = "%s|%s"%(scaffID,pos)
        mainDict[posID].isB(nReads)
        nSNPS_B += 1
    #####
    p.poll()
    
    # Performing the check on the ratio of snps
    try:
        r     = float(nSNPS_A) / float(nSNPS_B)
        ratio = min( r, 1.0/r )
    except ZeroDivisionError:
        ratio = -1.0
    #####
    
    # Typing the kmer locations
    oh_out = open( '%s/globalFileAnalysis_%s.dat'%(mainPath,fileBase), 'w' )
    outputString = '%s\t%d\t%d\t%.3f\t%.3f\n'%(fileBase,nSNPS_A,nSNPS_B,r,ratio)
    oh_out.write( outputString )
    oh_out.close()

    # Sorting and outputting the F1 calls
    scaffDict = {}
    for posID, tmpClass in mainDict.iteritems():
        scaffID, pos = posID.split('|')
        pos          = int(pos)
        outputString = tmpClass.generateOutputString()
        try:
            scaffDict[scaffID].append( (int(pos), outputString) )
        except KeyError:
            scaffDict[scaffID] = [ (int(pos), outputString) ]
        #####
    #####
    
    for scaffID, tmpList in scaffDict.iteritems():
        tmpList.sort()
        addSep = False
        for pos, item in tmpList:
            if ( item ):
                stdout.write( '%s\n'%item )
                addSep = True
            #####
        #####
        if ( addSep ): stdout.write( sepString )
    #####

    
#==============================================================
if ( __name__ == '__main__' ):
    real_main()
