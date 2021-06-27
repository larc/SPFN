import sys
import h5py
import numpy as np

f_xyz = sys.argv[1] + '.xyz'
f_h5 = sys.argv[1] + '.h5'
f_off = sys.argv[1] + '.off'
print(f_xyz, f_h5, f_off)

xyz = np.genfromtxt(f_xyz, delimiter=' ', dtype = float)[:, :3]

h5 = h5py.File(f_h5)
normals = h5['normal_per_point']
types = h5['type_per_point']

colors = [' 255 0 0 0 ', ' 0 255 0 0 ', ' 0 0 255 0 ', ' 255 255 0 0 ']

size = len(normals)

off = open(f_off, 'w')
off.write('NCOFF\n')
off.write(str(size) + ' 0 0\n')

for p in range(0, size):
	off.write(' '.join(map(str, xyz[p])) + colors[types[p]] + ' '.join(map(str, normals[p])) + '\n')

off.close()

