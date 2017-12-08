import numpy as np

untung = np.random.normal([25000, 50000, 150500, 100000])
mean = np.mean(untung)
median = np.median(untung)
print('Untung: %s' % untung)
print('Nilai mean: %s' % mean)
print('Nilai median: %s' % median)
