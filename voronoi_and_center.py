import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.spatial
import sys
from scipy.spatial import Voronoi
from scipy.spatial import voronoi_plot_2d
import time


class partition:
    def __init__(self, towers, ext):
        self.towers = towers
        self.ext = ext

    def gen_vor(self):
        n_towers = len(self.towers)
        tower_u = np.zeros([n_towers, 2])
        tower_d = np.zeros([n_towers, 2])
        tower_l = np.zeros([n_towers, 2])
        tower_r = np.zeros([n_towers, 2])
        tower_ru = np.zeros([n_towers, 2])
        tower_rd = np.zeros([n_towers, 2])
        tower_lu = np.zeros([n_towers, 2])
        tower_ld = np.zeros([n_towers, 2])
        for i in range(n_towers):
            tower_u[i, 0] = self.towers[i, 0]
            tower_u[i, 1] = 2 * self.ext - self.towers[i, 1]
            tower_d[i, 0] = self.towers[i, 0]
            tower_d[i, 1] = -self.towers[i, 1]
            tower_l[i, 1] = self.towers[i, 1]
            tower_l[i, 0] = -self.towers[i, 0]
            tower_r[i, 1] = self.towers[i, 1]
            tower_r[i, 0] = 2 * self.ext - self.towers[i, 0]
            tower_lu[i, 0] = -self.towers[i, 0]
            tower_lu[i, 1] = 2 * self.ext - self.towers[i, 1]
            tower_ld[i, 0] = -self.towers[i, 0]
            tower_ld[i, 1] = -self.towers[i, 1]
            tower_ru[i, 1] = 2 * self.ext - self.towers[i, 1]
            tower_ru[i, 0] = 2 * self.ext - self.towers[i, 0]
            tower_rd[i, 1] = -self.towers[i, 1]
            tower_rd[i, 0] = 2 * self.ext - self.towers[i, 0]
        tower_all = np.concatenate(
            (self.towers, tower_u, tower_r, tower_d, tower_l, tower_ld, tower_lu, tower_rd, tower_ru), axis=0)
        vor = Voronoi(points=tower_all)
        return vor

    # vertices_list = [] for i in range(len(vor.vertices)): if vor.vertices[i,0] <= ext and vor.vertices[i,0] >= 0 and
    # vor.vertices[i,1] <= ext and vor.vertices[i,1] >= 0: vertices_list.append(list(vor.vertices[i]))

    def save_region(self):
        save_region = []
        save_ver_i = []
        vor = self.gen_vor()
        for i in vor.point_region:
            flag = 1
            for j in vor.regions[i]:
                if -0.1 <= vor.vertices[j][0] <= self.ext + 0.1 and -0.1 <= vor.vertices[j][1] <= self.ext + 0.1:
                    flag = flag * 1
                else:
                    flag = 0
            if flag != 0:
                save_region.append(i)
                for k in vor.regions[i]:
                    save_ver_i.append(k)
        # for k in save_ver_i:
        #     plt.scatter(vor.vertices[k][0],vor.vertices[k][1])
        # plt.axis([0,ext,0,ext])
        # plt.show()
        # plt.figure(2)

        center_list = []
        for k in save_region:
            point = []
            for i in vor.regions[k]:
                point.append(vor.vertices[i])
            # point.append(vor.vertices[0])
            point = np.array(point)
            center = self.get_centerpoint(point)
            center_list.append(center)
        return center_list, vor

    def get_centerpoint(self,lis):
        area = 0.0
        x, y = 0.0, 0.0
        a = len(lis)
        for i in range(a):
            lat = lis[i][0]  # weidu
            lng = lis[i][1]  # jingdu
            if i == 0:
                lat1 = lis[-1][0]
                lng1 = lis[-1][1]
            else:
                lat1 = lis[i - 1][0]
                lng1 = lis[i - 1][1]
            fg = (lat * lng1 - lng * lat1) / 2.0
            area += fg
            x += fg * (lat + lat1) / 3.0
            y += fg * (lng + lng1) / 3.0
        x = x / area
        y = y / area
        return [x, y]
# 找出region
# 找出vertex
# 算出cv
