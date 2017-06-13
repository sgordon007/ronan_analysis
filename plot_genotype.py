import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('BhD1.BTNCA.11436.8.207067.ACTCGCT-TATCCTC.fastq_calling.bed.bedgraph', sep='\t', header=None, lineterminator='\n')
df.columns = ['chr', 'start', 'stop', 'UCXX', 'PNWH', 'HET']
test_data = df.head()
print test_data

to_subset = ['UCXX', 'PNWH', 'HET']
df2 = df[to_subset]

UCXX = (df['start'], df['UCXX'])
PNWH = (df['start'], df['PNWH'])
HET = (df['start'], df['HET'])

data = (UCXX, PNWH, HET)
colors = ("red", "green", "blue")
groups = ("UCXX", "PNWH", "HET")

# # Create a area plot
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1, axisbg="1.0")
# df2.plot(kind='area', stacked=False)
# plt.show()


### this alternative plot scatterplot OK
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, axisbg="1.0")
for data, color, group in zip(data, colors, groups):
    x, y = data
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)

plt.title('Matplot scatter plot')
plt.legend(loc=2)
plt.show()





#
# df2 = DataFrame(df, index=
#
# plt.figure(); df.plot();

# test_data2 = df.head()
# print test_data2

# x = df['start']
#
# l1 = list(df['BTNCA'])
# l2 = list(df['BTNCX'])
# l3 = list(df['BTNGT'])
#
# l1d = pd.DataFrame(
#     {'coord': x,
#      'BTNCA': l1,
#      'l3d': lst3
#     })

# plt.figure(); df.plot();

# l1 = list([x, l1])
# N =10
# for N in l1:
#     print l1[0,1]

