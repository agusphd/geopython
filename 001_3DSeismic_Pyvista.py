import pyvista as pv
import numpy as np

values = np.load('./DATA/volvesmall.npy')

grid = pv.UniformGrid()
grid.dimensions = values.shape
grid.origin = (0, 0, 0)
grid.spacing = (1, 1, 1)  # These are the cell sizes along each axis
grid.point_arrays["Amplitudes"] = values.flatten(order="F")

slices = grid.slice_orthogonal(x=50, y=50, z=50)
slices.plot(cmap='RdGy', clim=[-5, 5])