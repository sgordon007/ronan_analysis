__author__="Jerry Jenkins, sgordon@lbl.gov"
__date__ ="Created:  6/12/14"

## python /global/homes/s/sgordon/scripts/python/jerry/makeSubmissionFiles_BhybridumBroken.py

from os.path import split

#==============================================================
def writeScript( fullFileName, mainPath, genoType, kmerFile, merSize, bannedMarkers ):
    fileName  = '.'.join(split(fullFileName)[1].split('.')[:6])
    oh        = open( 'kmers.%s.%s.sh'%(fileName,genoType), 'w' )
    oh.write( '#!/bin/bash\n')
    oh.write( '## specify an email address\n')
    oh.write( '#$ -M sgordon@lbl.gov\n')
    oh.write( '## specify when to send the email when job is (a)borted, (b)egins or (e)nds normally\n')
    oh.write( '#$ -m ae\n')
    oh.write( '#$ -cwd\n')
    oh.write( '#$ -l h_rt=10:00:00\n')
    oh.write( '#$ -P plant-assembly.p\n') 
    oh.write( '## Job Starts Here\n')
    
    outputFileName = "%s/%s.%s.dat.bz2"%(mainPath,fileName,genoType)
    oh.write( "rm %s\n"%(outputFileName) )
    oh.write( "python /global/homes/s/sgordon/scripts/python/jerry/typeKmers.py %s %s %d %s | bzip2 -c > %s\n"%(fullFileName,kmerFile,merSize,bannedMarkers,outputFileName) )
    oh.close()
    
#==============================================================
def callingScript( fullFileName, mainPath, A, A_kmers, B, B_kmers, bannedMarkers ):
    fileName  = '.'.join(split(fullFileName)[1].split('.')[:6])
    oh        = open( 'calling.%s.sh'%(fileName), 'w' )
    oh.write( '#!/bin/bash\n')
    oh.write( '## specify an email address\n')
    oh.write( '#$ -M sgordon@lbl.gov\n')
    oh.write( '## specify when to send the email when job is (a)borted, (b)egins or (e)nds normally\n')
    oh.write( '#$ -m ae\n')
    oh.write( '#$ -cwd\n')
    oh.write( '#$ -l h_rt=3:00:00\n')
    oh.write( '#$ -P plant-assembly.p\n') 
    oh.write( '#$ -l ram.c=15G\n' )
    oh.write( '## Job Starts Here\n')
    
    out_1 = "%s/%s_calling.dat.bz2\n"%(mainPath,fileName)
    oh.write( "rm %s\n"%out_1 )
    
    out_2 = '%s/globalFileAnalysis_%s.dat\n'%(mainPath,fileName)
    oh.write( 'rm %s\n'%out_2 )
    
    oh.write( "python /global/homes/s/sgordon/scripts/python/jerry/calling_A_B.py %s %s %s %s %s %s %s | bzip2 -c > %s\n"%(fileName,A,A_kmers,B,B_kmers,mainPath,bannedMarkers,out_1) )
    
    oh.close()

#==============================================================
def real_main():
    
    mainPath = '/global/projectb/scratch/sgordon/ronan_data'
    
    
    A       = 'UCXX'
    A_kmers = '%s/UCXX_markers.fasta'%mainPath

    B       = 'PNWH'
    B_kmers = '%s/PNWH_markers.fasta'%mainPath
    
    kmerDict = { A:A_kmers, B:B_kmers }
    
    merSize  = 51
    
    ##sgordon@genepool11:/global/projectb/scratch/sgordon/polyploid_analysis/B_staceii_hybridum/hybridum_callingFiles/reapr_hybridum_calling_files$ head -n 2 H0035_kmers.fasta | tail -n 1 | wc
    ##  1       1      51
    
    bannedMarkers = '%s/bannedMarkers.dat'%mainPath
    
    for line in open('finalMappingLibSet.dat'):

        fullFileName = line.strip()
        
        # ##### (1) Run the lines below first
        # for genoType, kmerFile in kmerDict.iteritems():
        #     writeScript( fullFileName, mainPath, genoType, kmerFile, merSize, bannedMarkers )
        #  #####

        ### (2) Then run the lines below second
        callingScript( fullFileName, mainPath, A, kmerDict[A], B, kmerDict[B], bannedMarkers )

        ####

    #####
    
#==============================================================
if ( __name__ == '__main__' ):
    real_main()


