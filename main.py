import numpy as np
from scipy.spatial import voronoi_plot_2d
import matplotlib.pyplot as plt
from voronoi_and_center import partition

# 创建多边形
# rectangle
ext = 100
n_towers = 20
np.random.seed(10)
towers = np.random.rand(n_towers, 2) * ext
ri = np.random.random(n_towers) * ext  # initialization of ri
# partition
# 找到cv
cen, vor = partition(towers, ext).save_region()  # updating partition
# 计算hv
# 移到cv
step = 0
while step < 10:
    plt.figure(step)
    center, vor = partition(towers, ext).save_region()
    towers = np.array(center)
    voronoi_plot_2d(vor)
    plt.axis([0, ext, 0, ext])
    for i in range(len(center)):
        plt.scatter(center[i][0], center[i][1], marker='o', c='r')
    plt.show()
    step += 1
print(towers)
# 继续划分
# 计算hv
