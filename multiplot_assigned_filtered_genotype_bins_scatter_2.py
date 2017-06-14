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
    # df1.columns = ['chr', 'start', 'stop', 'assigned_geno']

    # subset columns to plot for lib1
    # to_subset = ['start', 'assigned_geno']
    df1 = df1.iloc[:, [1, 3]]
    test_data = df1.head()
    print test_data

    print(df1)

    # df1 = df1[[1], [3]]
    # df1.start = df1.start.astype(float).fillna(0.0)
    # df1.start.apply(pd.to_numeric)
    # df1['start'] = df1['start'].apply(pd.to_numeric, errors='coerce')

    df1_UNK = df1[df1.iloc[:, 1].str.contains("UNK")]
    df1_UNK.replace(['UNK', 'UCXX', 'PNWH', 'HET'], [1.0, 1.0, -1.0, 0.0], inplace=True)
    df1_UCXX = df1[df1.iloc[:, 1].str.contains("UCXX")]
    df1_UCXX.replace(['UNK', 'UCXX', 'PNWH', 'HET'], [1.0, 1.0, -1.0, 0.0], inplace=True)
    df1_PNWH = df1[df1.iloc[:, 1].str.contains("PNWH")]
    df1_PNWH.replace(['UNK', 'UCXX', 'PNWH', 'HET'], [1.0, 1.0, -1.0, 0.0], inplace=True)
    df1_HET = df1[df1.iloc[:, 1].str.contains("HET")]
    df1_HET.replace(['UNK', 'UCXX', 'PNWH', 'HET'], [1.0, 1.0, -1.0, 0.0], inplace=True)

    print(df1_UNK)

    df1_UCXX = df1_UCXX.astype(float)
    df1_PNWH = df1_PNWH.astype(float)
    df1_HET = df1_HET.astype(float)

    UCXX = (df1_UCXX.iloc[:, 0], df1_UCXX.iloc[:, 1])
    PNWH = (df1_PNWH.iloc[:, 0], df1_PNWH.iloc[:, 1])
    HET = (df1_HET.iloc[:, 0], df1_HET.iloc[:, 1])


    test_data = df1_UCXX.head()
    print test_data

    data = (UCXX, PNWH, HET)
    colors = ("red", "green", "blue")
    groups = ("UCXX", "PNWH", "HET")

    ## this alternative plot scatterplot OK
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    for data, color, group in zip(data, colors, groups):
        x, y = data
        ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)

    plt.title('Matplot scatter plot')
    plt.legend(loc=2)
    plt.show()

    # # Create a area plot for lib1
    # fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(7,11))
    # df1_UCXX.plot(ax=axes[0]); axes[0].set_title('1xRXN'); plt.xlabel('physical distance (x10 kbp)'); plt.ylabel('genotype freq')

    ###test


    #
    # # read in the second lib
    # df2 = pd.read_csv(b, sep='\t', header=None, lineterminator='\n')
    # df2.columns = ['chr', 'start', 'stop', 'assigned_geno']
    # test_data = df2.head()
    # print test_data
    # # subset columns to plot for lib1
    # to_subset = ['assigned_geno']
    # df2 = df2[to_subset]
    # df2.replace(['UNK', 'UCXX', 'PNWH', 'HET'], [0.2, 1.0, -1.0, 0.0], inplace=True)
    #
    # # Create a area plot for lib2
    # df2.plot(ax=axes[1]); axes[1].set_title('10xRXN'); plt.xlabel('physical distance (x10 kbp)'); plt.ylabel('genotype freq')
    #
    # # read in the third lib
    # df3 = pd.read_csv(c, sep='\t', header=None, lineterminator='\n')
    # df3.columns = ['chr', 'start', 'stop', 'assigned_geno']
    # test_data = df3.head()
    # print test_data
    # # subset columns to plot for lib1
    # to_subset = ['assigned_geno']
    # df3 = df3[to_subset]
    # df3.replace(['UNK', 'UCXX', 'PNWH', 'HET'], [0.2, 1.0, -1.0, 0.0], inplace=True)
    #
    # # Create a area plot for lib1
    # df3.plot(ax=axes[2]); axes[2].set_title('20xRXN'); plt.xlabel('physical distance (x10 kbp)'); plt.ylabel('genotype freq')
    # ### alt for area: df3.plot(kind='area', stacked=False, ax=axes[2]); axes[2].set_title('C')

    # plt.show()
    # plt.savefig('multi_data.png')






if __name__ == "__main__":
    geno_multi_read(a=str(sys.argv[1]), b=str(sys.argv[2]), c=str(sys.argv[3]))


# geno_multi_read('BhD1.BTNCA.11436.8.207067.ACTCGCT-TATCCTC.fastq_calling.bed.bedgraph', 'BhD1.BTNCX.11436.8.207067.GGAGCTA-CGTCTAA.fastq_calling.bed.bedgraph', 'BhD1.BTNGT.11436.8.207067.CGGAGCC-GTAAGGA.fastq_calling.bed.bedgraph')