import numpy as np
from statistics import mode

umur = np.random.randint(18, high=90, size=600)
print('umur = %s' % umur)
mode = mode(umur)
print('mode umur = %s' % mode)


#using scipy
from scipy import stats
mode2 = stats.mode(umur)
mode_with_scipy = mode2.mode[0]
total_mode_with_scipy = mode2.count
print('mode umur scipy: %s' % mode_with_scipy)
print('total mode umur scipy: %s' % total_mode_with_scipy[0])
