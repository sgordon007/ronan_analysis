__author__ = 'sgordon007'

"""
plot the genotype data with multiple subplots, one per lib.
"""

# BTNCA.11436.8.207067.ACTCGCT-TATCCTC.fastq_calling.sorted.bedgraph BTNCX.11436.8.207067.GGAGCTA-CGTCTAA.fastq_calling.sorted.bedgraph BTNGT.11436.8.207067.CGGAGCC-GTAAGGA.fastq_calling.sorted.bedgraph

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys



def geno_multi_read(a, b, c):

    # read in the first lib
    print 'working on file:' + a
    df1 = pd.read_csv(a, sep='\t', header=None, lineterminator='\n')
    df1.columns = ['chr', 'start', 'stop', 'assigned_geno']
    test_data = df1.head()
    print test_data
    # subset columns to plot for lib1
    to_subset = ['assigned_geno']
    df1 = df1[to_subset]
    df1.replace(['UNK', 'UCXX', 'PNWH', 'HET'], [0.2, 1.0, 2.0, 0.0], inplace=True)

    # Create a area plot for lib1
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(7,11))
    df1.plot(ax=axes[0]); axes[0].set_title('1xRXN'); plt.xlabel('physical distance (x10 kbp)'); plt.ylabel('genotype freq')

    # read in the second lib
    df2 = pd.read_csv(b, sep='\t', header=None, lineterminator='\n')
    df2.columns = ['chr', 'start', 'stop', 'assigned_geno']
    test_data = df2.head()
    print test_data
    # subset columns to plot for lib1
    to_subset = ['assigned_geno']
    df2 = df2[to_subset]
    df2.replace(['UNK', 'UCXX', 'PNWH', 'HET'], [0.2, 1.0, 2.0, 0.0], inplace=True)

    # Create a area plot for lib2
    df2.plot(ax=axes[1]); axes[1].set_title('10xRXN'); plt.xlabel('physical distance (x10 kbp)'); plt.ylabel('genotype freq')

    # read in the third lib
    df3 = pd.read_csv(c, sep='\t', header=None, lineterminator='\n')
    df3.columns = ['chr', 'start', 'stop', 'assigned_geno']
    test_data = df3.head()
    print test_data
    # subset columns to plot for lib1
    to_subset = ['assigned_geno']
    df3 = df3[to_subset]
    df3.replace(['UNK', 'UCXX', 'PNWH', 'HET'], [0.2, 1.0, 2.0, 0.0], inplace=True)

    # Create a area plot for lib1
    df3.plot(ax=axes[2]); axes[2].set_title('20xRXN'); plt.xlabel('physical distance (x10 kbp)'); plt.ylabel('genotype freq')
    ### alt for area: df3.plot(kind='area', stacked=False, ax=axes[2]); axes[2].set_title('C')

    plt.show()
    plt.savefig('multi_data.png')



if __name__ == "__main__":
    geno_multi_read(a=str(sys.argv[1]), b=str(sys.argv[2]), c=str(sys.argv[3]))


# geno_multi_read('BhD1.BTNCA.11436.8.207067.ACTCGCT-TATCCTC.fastq_calling.bed.bedgraph', 'BhD1.BTNCX.11436.8.207067.GGAGCTA-CGTCTAA.fastq_calling.bed.bedgraph', 'BhD1.BTNGT.11436.8.207067.CGGAGCC-GTAAGGA.fastq_calling.bed.bedgraph')