__author__ = 'sgordon007'

import pybedtools
a = pybedtools.BedTool('a.bedgraph')
b = pybedtools.BedTool('b.bedgraph')
c = pybedtools.BedTool('c.bedgraph')
#print (a).count()

"""
print a.sort()
print b.sort()
print c.sort()
"""


aS = a.sort()
"""
bS = b.sort()
cS = c.sort()
"""


print aS

x = pybedtools.BedTool()
#>>> a = pybedtools.example_bedtool('a.bed')
#>>> b = pybedtools.example_bedtool('b.bed')
result = x.union_bedgraphs(i=[aS.fn, bS.fn, cS.fn], g="genome.filename")
print result

#bedAnalyze = BedTool('%s.bed'%(syntenicInputFiles[0][:syntenicInputFiles[0].rfind('.')])).sort()

    # old debug method...
    #stop=1 #pause here and drag bed file to new location

    ###########
    #return bedAnalyze # this is our BedTool object

#u = [a,b,c]
#print u
#uBG = pybedtools.bedtool.BedTool.union_bedgraphs(a)
