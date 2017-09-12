__author__ = 'sgordon007'

"""
plot the genotype data with multiple subplots, one per lib.
"""

# BTNCA.11436.8.207067.ACTCGCT-TATCCTC.fastq_calling.sorted.bedgraph BTNCX.11436.8.207067.GGAGCTA-CGTCTAA.fastq_calling.sorted.bedgraph BTNGT.11436.8.207067.CGGAGCC-GTAAGGA.fastq_calling.sorted.bedgraph

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys



def geno_multi_read(a, b, c, d):

    # read in the first lib
    print 'working on file:' + a
    df1 = pd.read_csv(a, sep='\t', header=None, lineterminator='\n')
    df1 = df1.iloc[:, [1, 3]]

    df1_UNK = df1[df1.iloc[:, 1].str.contains("UNK")]
    df1_UNK.replace(['UNK', 'UCXX', 'PNWH', 'HET'], [1.0, 1.0, -1.0, 0.0], inplace=True)
    df1_UCXX = df1[df1.iloc[:, 1].str.contains("UCXX")]
    df1_UCXX.replace(['UNK', 'UCXX', 'PNWH', 'HET'], [1.0, 1.0, -1.0, 0.0], inplace=True)
    df1_PNWH = df1[df1.iloc[:, 1].str.contains("PNWH")]
    df1_PNWH.replace(['UNK', 'UCXX', 'PNWH', 'HET'], [1.0, 1.0, -1.0, 0.0], inplace=True)
    df1_HET = df1[df1.iloc[:, 1].str.contains("HET")]
    df1_HET.replace(['UNK', 'UCXX', 'PNWH', 'HET'], [1.0, 1.0, -1.0, 0.0], inplace=True)

    df1_UCXX = df1_UCXX.astype(float)
    df1_PNWH = df1_PNWH.astype(float)
    df1_HET = df1_HET.astype(float)

    UCXX = (df1_UCXX.iloc[:, 0], df1_UCXX.iloc[:, 1].cumsum())
    PNWH = (df1_PNWH.iloc[:, 0], df1_PNWH.iloc[:, 1].cumsum())
    HET = (df1_HET.iloc[:, 0], df1_HET.iloc[:, 1].cumsum())

    data = (UCXX, PNWH, HET)
    colors = ("red", "green", "blue")
    groups = ("UCXX", "PNWH", "HET")

    ### try to modify plot type:
    fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(7, 11))
    ax=axes[0]
    ax.set_title('previous data')
    # plt.xlabel('physical distance (x10 kbp)')
    # plt.ylabel('genotype freq')

    for data, color, group in zip(data, colors, groups):
        x, y = data
        axes[0].scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)

    # ### maybe this should go at the end:
    # plt.title('Matplot scatter plot')
    # plt.legend(loc=2)
    # plt.show()


    # read in the second lib
    df2 = pd.read_csv(b, sep='\t', header=None, lineterminator='\n')
    df2 = df2.iloc[:, [1, 3]]

    df2_UNK = df2[df2.iloc[:, 1].str.contains("UNK")]
    df2_UNK.replace(['UNK', 'UCXX', 'PNWH', 'HET'], [1.0, 1.0, -1.0, 0.0], inplace=True)
    df2_UCXX = df2[df2.iloc[:, 1].str.contains("UCXX")]
    df2_UCXX.replace(['UNK', 'UCXX', 'PNWH', 'HET'], [1.0, 1.0, -1.0, 0.0], inplace=True)
    df2_PNWH = df2[df2.iloc[:, 1].str.contains("PNWH")]
    df2_PNWH.replace(['UNK', 'UCXX', 'PNWH', 'HET'], [1.0, 1.0, -1.0, 0.0], inplace=True)
    df2_HET = df2[df2.iloc[:, 1].str.contains("HET")]
    df2_HET.replace(['UNK', 'UCXX', 'PNWH', 'HET'], [1.0, 1.0, -1.0, 0.0], inplace=True)

    df2_UCXX = df2_UCXX.astype(float)
    df2_PNWH = df2_PNWH.astype(float)
    df2_HET = df2_HET.astype(float)

    UCXX = (df2_UCXX.iloc[:, 0], df2_UCXX.iloc[:, 1].cumsum())
    PNWH = (df2_PNWH.iloc[:, 0], df2_PNWH.iloc[:, 1].cumsum())
    HET = (df2_HET.iloc[:, 0], df2_HET.iloc[:, 1].cumsum())

    data = (UCXX, PNWH, HET)
    colors = ("red", "green", "blue")
    groups = ("UCXX", "PNWH", "HET")

    ### try to modify plot type:
    # fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(7, 11))
    ax=axes[1]
    ax.set_title('1xRXN')
    # plt.xlabel('physical distance (x10 kbp)')
    # plt.ylabel('genotype freq')

    for data, color, group in zip(data, colors, groups):
        x, y = data
        ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)

### maybe this should go at the end:
    # plt.title('Matplot scatter plot')
    # plt.legend(loc=2)
    # plt.show()

    # # Create a area plot for lib2
    # df2.plot(ax=axes[1]); axes[1].set_title('10xRXN'); plt.xlabel('physical distance (x10 kbp)'); plt.ylabel('genotype freq')

    # read in the third lib
    df3 = pd.read_csv(c, sep='\t', header=None, lineterminator='\n')

    df3 = df3.iloc[:, [1, 3]]

    df3_UNK = df3[df3.iloc[:, 1].str.contains("UNK")]
    df3_UNK.replace(['UNK', 'UCXX', 'PNWH', 'HET'], [1.0, 1.0, -1.0, 0.0], inplace=True)
    df3_UCXX = df3[df3.iloc[:, 1].str.contains("UCXX")]
    df3_UCXX.replace(['UNK', 'UCXX', 'PNWH', 'HET'], [1.0, 1.0, -1.0, 0.0], inplace=True)
    df3_PNWH = df3[df3.iloc[:, 1].str.contains("PNWH")]
    df3_PNWH.replace(['UNK', 'UCXX', 'PNWH', 'HET'], [1.0, 1.0, -1.0, 0.0], inplace=True)
    df3_HET = df3[df3.iloc[:, 1].str.contains("HET")]
    df3_HET.replace(['UNK', 'UCXX', 'PNWH', 'HET'], [1.0, 1.0, -1.0, 0.0], inplace=True)

    df3_UCXX = df3_UCXX.astype(float)
    df3_PNWH = df3_PNWH.astype(float)
    df3_HET = df3_HET.astype(float)

    UCXX = (df3_UCXX.iloc[:, 0], df3_UCXX.iloc[:, 1].cumsum())
    PNWH = (df3_PNWH.iloc[:, 0], df3_PNWH.iloc[:, 1].cumsum())
    HET = (df3_HET.iloc[:, 0], df3_HET.iloc[:, 1].cumsum())

    data = (UCXX, PNWH, HET)
    colors = ("red", "green", "blue")
    groups = ("UCXX", "PNWH", "HET")

    ### try to modify plot type:
    # fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(7, 11))
    ax = axes[2]
    ax.set_title('10xRXN')
    # plt.xlabel('physical distance (x10 kbp)')
    # plt.ylabel('genotype freq')

    for data, color, group in zip(data, colors, groups):
        x, y = data
        ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group); plt.xlabel('physical distance (x10 kbp)'); plt.ylabel('genotype freq')

    # read in the fourth lib
    df4 = pd.read_csv(d, sep='\t', header=None, lineterminator='\n')

    df4 = df4.iloc[:, [1, 3]]

    df4_UNK = df4[df4.iloc[:, 1].str.contains("UNK")]
    df4_UNK.replace(['UNK', 'UCXX', 'PNWH', 'HET'], [1.0, 1.0, -1.0, 0.0], inplace=True)
    df4_UCXX = df4[df4.iloc[:, 1].str.contains("UCXX")]
    df4_UCXX.replace(['UNK', 'UCXX', 'PNWH', 'HET'], [1.0, 1.0, -1.0, 0.0], inplace=True)
    df4_PNWH = df4[df4.iloc[:, 1].str.contains("PNWH")]
    df4_PNWH.replace(['UNK', 'UCXX', 'PNWH', 'HET'], [1.0, 1.0, -1.0, 0.0], inplace=True)
    df4_HET = df4[df4.iloc[:, 1].str.contains("HET")]
    df4_HET.replace(['UNK', 'UCXX', 'PNWH', 'HET'], [1.0, 1.0, -1.0, 0.0], inplace=True)

    df4_UCXX = df4_UCXX.astype(float)
    df4_PNWH = df4_PNWH.astype(float)
    df4_HET = df4_HET.astype(float)

    UCXX = (df4_UCXX.iloc[:, 0], df4_UCXX.iloc[:, 1].cumsum())
    PNWH = (df4_PNWH.iloc[:, 0], df4_PNWH.iloc[:, 1].cumsum())
    HET = (df4_HET.iloc[:, 0], df4_HET.iloc[:, 1].cumsum())

    data = (UCXX, PNWH, HET)
    colors = ("red", "green", "blue")
    groups = ("UCXX", "PNWH", "HET")

    ### try to modify plot type:
    # fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(7, 11))
    ax = axes[3]
    ax.set_title('20xRXN')
    # plt.xlabel('physical distance (x10 kbp)')
    # plt.ylabel('genotype freq')

    for data, color, group in zip(data, colors, groups):
        x, y = data
        ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group);
        plt.xlabel('physical distance (x10 kbp)');
        plt.ylabel('genotype freq')


    # # Create a area plot for lib1
    # df3.plot(ax=axes[2]); axes[2].set_title('20xRXN'); plt.xlabel('physical distance (x10 kbp)'); plt.ylabel('genotype freq')
    # ### alt for area: df3.plot(kind='area', stacked=False, ax=axes[2]); axes[2].set_title('C')

    plt.show()
    plt.savefig('multi_data.png')






if __name__ == "__main__":
    geno_multi_read(a=str(sys.argv[1]), b=str(sys.argv[2]), c=str(sys.argv[3]), d=str(sys.argv[3]))


# geno_multi_read('BhD1.BTNCA.11436.8.207067.ACTCGCT-TATCCTC.fastq_calling.bed.bedgraph', 'BhD1.BTNCX.11436.8.207067.GGAGCTA-CGTCTAA.fastq_calling.bed.bedgraph', 'BhD1.BTNGT.11436.8.207067.CGGAGCC-GTAAGGA.fastq_calling.bed.bedgraph')