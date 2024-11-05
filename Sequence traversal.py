"""
二叉树遍历搜索，随机生成几个点，然后指定其中一个点，给出这个点所在的位置，并且把树和划分的图表示出来
采用层序遍历法
"""
from time import perf_counter

import numpy as np
from fontTools.misc.cython import returns

from function import create_tree
from function import n
from function import remove_element
import matplotlib.pyplot as plt
from function import random_point
from function import add_line_to_graph


v = 1
c = int(input("请输入需要搜索的点的序号："))  # 注意：点的序号从0开始
# c = 0
center = [[0, 0]]
add = [0]

for i in range(n+1):
    add.append(50/(2**(i+1)))

# 生成10个5x5的随机二维数组
x, x1, x2, num = random_point()
print("随机生成的所有点的坐标为：",x)
print("选取的点坐标为：",x[c])

tree = create_tree(n, v)  # 创造了一个n层的四叉树

# 数组中已经给定了第一层的center是[0,0]，所以这里直接从第二层开始插入center
# 层序遍历，在第r+1层时，在哪个象限内

nod = []
if x[c][0] > center[0][0] and x[c][1] > center[0][1]:
    # print("在第一象限内")
    center.append([center[0][0] + add[0], center[0][1] + add[0]])
    # print(0 + 1, center[1:])
    for i in range(num):
        if x[i][0] > center[0][0] and x[i][1] > center[0][1] and i != c:
            nod.append(i)
    # print("第", nod, "个点")

if x[c][0] < center[0][0] and x[c][1] > center[0][1]:
    # print("在第二象限内")
    center.append([center[0][0] - add[0], center[0][1] + add[0]])
    # print(0 + 1, center[1:])
    for i in range(num):
        if x[i][0] < center[0][0] and x[i][1] > center[0][1] and i != c:
            nod.append(i)
    # print("第", nod, "个点")

if x[c][0] < center[0][0] and x[c][1] < center[0][1]:
    # print("在第三象限内")
    center.append([center[0][0] - add[0], center[0][1] - add[0]])
    # print(0 + 1, center[1:])
    for i in range(num):
        if x[i][0] < center[0][0] and x[i][1] < center[0][1] and i != c:
            nod.append(i)
    # print("第", nod, "个点")

if x[c][0] > center[0][0] and x[c][1] < center[0][1]:
    # print("在第四象限内")
    center.append([center[0][0] + add[0], center[0][1] - add[0]])
    # print(0 + 1, center[1:])
    for i in range(num):
        if x[i][0] > center[0][0] and x[i][1] < center[0][1] and i != c:
            nod.append(i)
    # print("第", nod, "个点")


# 注意点的序号是0，1，2...
nod_ = nod.copy()
# 设置循环变量
count = 0
for k in range(1, n):
        count += 1
        nod = nod_.copy()
        if x[c][0] > center[k][0] and x[c][1] > center[k][1]:
            print("在第",k,"层遍历过程时，该点在第一象限内")
            center.append([center[k][0] + add[k], center[k][1] + add[k]])
            # print(k, center[1:-1])

            if nod:
                for i in range(len(nod)):
                    p = nod[i]
                    if x[p][0] <= center[k][0] or x[p][1] <= center[k][1]:
                        nod_ = remove_element(nod_, p)
                if nod_:
                    print("生成的第", nod_, "个点同样也在该象限内")
                else:
                    print("该象限内不存在其他点")
                    break
            else:
                print("该象限内不存在其他点")
                break

        if x[c][0] < center[k][0] and x[c][1]  > center[k][1]:
            print("在第",k,"层遍历过程时，该点在第二象限内")
            center.append([center[k][0] - add[k], center[k][1] + add[k]])
            # print(k, center[1:-1])

            if nod:
                for i in range(len(nod)):
                    p = nod[i]
                    if x[p][0] >= center[k][0] or x[p][1] <= center[k][1]:
                        nod_ = remove_element(nod_, p)
                if nod_:
                    print("生成的第", nod_, "个点同样也在该象限内")
                else:
                    print("该象限内不存在其他点")
                    break
            else:
                print("该象限内不存在其他点")
                break

        if x[c][0] < center[k][0] and x[c][1]  < center[k][1]:
            print("在第",k,"层遍历过程时，该点在第三象限内")
            center.append([center[k][0] - add[k], center[k][1] - add[k]])
            # print(k, center[1:-1])
            if nod:
                for i in range(len(nod)):
                    p = nod[i]
                    if x[p][0] >= center[k][0] or x[p][1] >= center[k][1]:
                        nod_ = remove_element(nod_, p)
                if nod_:
                    print("生成的第", nod_, "个点同样也在该象限内")
                else:
                    print("该象限内不存在其他点")
                    break
            else:
                print("该象限内不存在其他点")
                break

        if x[c][0] > center[k][0] and x[c][1] < center[k][1]:
            print("在第",k,"层遍历过程时，该点在第四象限内")
            center.append([center[k][0] + add[k], center[k][1] - add[k]])
            # print(k, center[1:-1])
            if nod:
                for i in range(len(nod)):
                    p = nod[i]
                    if x[p][0] <= center[k][0] or x[p][1] >= center[k][1]:
                        nod_ = remove_element(nod_, p)
                if nod_:
                    print("生成的第", nod_, "个点同样也在该象限内")
                else:
                    print("该象限内不存在其他点")
                    break
            else:
                print("该象限内不存在其他点")
                break
print("在第",count,"层遍历中搜索到这个点")

fig, ax = plt.subplots(figsize=(6, 6))
plt.title("50x50 graph")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")

ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)

plt.scatter(x1, x2, color='blue', marker='o', s=10)

# 在图形上添加直线
add_line_to_graph(100, (0, 0), ax)
for i in range(count):
    add_line_to_graph(2*add[i], (center[i+1][0],center[i+1][1]), ax)
# 显示图形
# 显示图形
plt.show()


