import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('BhD1.BTNCA.BTNCX.BTNGT.union.bedgraph', sep='\t', header=None, lineterminator='\n')
df.columns = ['chr', 'start', 'stop', 'BTNCA', 'BTNCX', 'BTNGT']
test_data = df.head()
print test_data


BTNCA = (df['start'], df['BTNCA'])

BTNCX = (df['start'], df['BTNCX'])

BTNGT = (df['start'], df['BTNGT'])

data = (BTNCA, BTNCX, BTNGT)
colors = ("red", "green", "blue")
groups = ("BTNCA", "BTNCX", "BTNGT")

# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, axisbg="1.0")

for data, color, group in zip(data, colors, groups):
    x, y = data
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)

plt.title('Matplot scatter plot')
plt.legend(loc=2)
plt.show()


# g2 = (0.4 + 0.3 * np.random.rand(N), 0.5 * np.random.rand(N))
# g3 = (0.3 * np.random.rand(N), 0.3 * np.random.rand(N))
#
# data = (g1, g2, g3)
# colors = ("red", "green", "blue")
# groups = ("coffee", "tea", "water")



#
# to_subset = ['start', 'BTNCA', 'BTNCX', 'BTNGT']
#
# df = df[to_subset]
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

#


#
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Create data
# N = 60
# g1 = (0.6 + 0.6 * np.random.rand(N), np.random.rand(N))
# g2 = (0.4 + 0.3 * np.random.rand(N), 0.5 * np.random.rand(N))
# g3 = (0.3 * np.random.rand(N), 0.3 * np.random.rand(N))
#
# data = (g1, g2, g3)
# colors = ("red", "green", "blue")
# groups = ("coffee", "tea", "water")
#
# # Create plot
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1, axisbg="1.0")
#
# for data, color, group in zip(data, colors, groups):
#     x, y = data
#     ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
#
# plt.title('Matplot scatter plot')
# plt.legend(loc=2)
# plt.show()
