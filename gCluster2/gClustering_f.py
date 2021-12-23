import math
import numpy as np
import matplotlib.pyplot as plt


def readData(path):
    cell = []
    numberOfCells = []
    # path = 'H_data.txt'

    with open(path) as f:
        for line in f.readlines():
            s = line.split(' , ')
            cell.append(int(s[0]))
            cell.append(int(s[1]))
            cell.append(float(s[2]))
            cell.append(float(s[3]))
            cell.append(int(s[4]))
            numberOfCells.append(int(s[4]))
    cellListToArray = np.array(cell)
    cells = cellListToArray.reshape(-1, 5)
    return cells, numberOfCells


def dist(ci, cj, e):
    # d = math.sqrt((ci[2] * e - cj[2] * e)**2 + (ci[3] * e - cj[3] * e)**2)
    # d = ((ci[2] / (1 / e) - cj[2] / (1 / e)) ** 2 + (ci[3] / (1 / e) - cj[3] / (1 / e)) ** 2) ** 1/2
    d = (((ci[2]*e - cj[2]*e) ** 2) + ((ci[3]*e - cj[3]*e) ** 2)) ** 1 / 2
    return d


def calForce(ci, cj, e, ct_max):
    n = (ci[4] / ct_max) * (cj[4] / ct_max)
    d = dist(ci, cj, e)
    result = (n / (d ** 2))
    return result


def Gcluster(H, cell_size, min_force, min_cells, max_cell_value):
    maxCellValue = max(max_cell_value)
    g = np.zeros([cell_size, cell_size])
    t = 1
    n = 1
    count = np.zeros([H.shape[0]])

    for h in H:
        if g[int(h[0]), int(h[1])] == 0:
            g[int(h[0]), int(h[1])] = n
            # count[n] += 1
            n += 1
        for hh in H[t:]:
            if abs(int(h[0]) - int(hh[0])) <= 1 and abs(int(h[1]) - int(hh[1])) <= 1:
                F = calForce(h, hh, cell_size, maxCellValue)
                if F >= min_force:
                    g[int(hh[0]), int(hh[1])] = g[int(h[0]), int(h[1])]
        t += 1

    for i in range(g.shape[0]):
        for j in range(g.shape[1]):
            count[int(g[i][j])] += 1

    for idx in range(0, count.shape[0]):
        if count[idx] <= min_cells:
            for i in range(0, g.shape[0]):
                for j in range(0, g.shape[1]):
                    if g[i][j] == idx:
                        g[i][j] = 0
    return g


def visualize(g):
    x = []
    y = []
    colors = []
    for xx in range(g.shape[0]):
        for yy in range(g.shape[1]):
            if g[xx][yy] != 0:
                x.append(int(xx))
                y.append(int(yy))
                colors.append(int(g[xx][yy]))

    colorsToArray = np.array(colors)
    normal = plt.Normalize(colorsToArray.min(), colorsToArray.max())
    cm = plt.cm.jet(normal(colorsToArray))

    plt.scatter(x, y, marker="o", s=10, c=colors, cmap='jet', zorder=2)

    for i, label in enumerate(colors):
        plt.annotate(label, (x[i], y[i]))
        plt.fill_between([x[i], x[i] + 1], y[i], y[i] + 1, facecolor=cm[i])

    x_ticks = np.arange(0, g.shape[0], 1)
    y_ticks = np.arange(0, g.shape[1], 1)
    plt.xticks(x_ticks)
    plt.yticks(y_ticks)
    plt.xlim([0, g.shape[0]])
    plt.ylim([0, g.shape[1]])
    plt.grid()
    plt.show()
