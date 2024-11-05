# 定义四叉树
class TreeNode:
    def __init__(self, value=0, k1=None, k2=None, k3=None, k4=None):
        self.value = value
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.k4 = k4

    def v(self):
        return self.value

    def next(self):
        return TreeNode(value=self.value + 1).value

# n为外部输入的四叉树层数
# 按层k和值value创造树节点及其子节点
n = int(input("四叉树层数："))

def create_tree(k, value):
    if n + n < k:
        return None
    node = TreeNode(value)
    node.k1 = create_tree(k + 1, value * 4 - 2)
    node.k2 = create_tree(k + 1, value * 4 - 1)
    node.k3 = create_tree(k + 1, value * 4 - 0)
    node.k4 = create_tree(k + 1, value * 4 + 1)

    return node

# n = 10
# v = 1

# tree = create_tree(n, v)
# print(tree.k1.k1.k1.k1.k1.k1.k1.k1.k1.k1.v())
# print(tree.v())
# print(tree.k1.next())
# print(tree.k1.v())

def remove_element(arr, element):
    if element in arr:
        arr.remove(element)
    return arr

def remove_element(arr, element):
    if element in arr:
        arr.remove(element)
    return arr

# 测试函数
'''
test_array = [1, 2, 3, 4, 5]
test_array = remove_element(test_array, 6)  # 数组中没有元素 6，应该保持不变

print(test_array)
'''

# 一个生成随机点的小函数
def random_point():
    import numpy as np
    num = int(input("请输入随机点的数量："))  # 生成点的数量
    x = [np.random.uniform(-50, 50, size=2) for _ in range(num)]
    # x = [[2,2], [3,3], [40, 40], [6, 7]]
    x1 = []
    x2 = []
    for i in range(num):
        x1.append(x[i][0])
        x2.append(x[i][1])
    return x,x1,x2,num


def add_line_to_graph(length, midpoint, ax):
    """
    在给定的图形上添加一条已知长度和中点坐标的直线。

    :param length: 直线的长度
    :param midpoint: 中点的坐标，格式为 (x, y)
    :param ax: 图形上的坐标轴对象
    """
    # 计算端点坐标
    left_point = (midpoint[0] - length / 2, midpoint[1])
    right_point = (midpoint[0] + length / 2, midpoint[1])
    up_point = (midpoint[0], midpoint[1] + length / 2)
    down_point = (midpoint[0], midpoint[1]-length / 2)

    # 在图形上绘制直线
    ax.plot([left_point[0], right_point[0]], [left_point[1], right_point[1]], color='green', label='Line')
    ax.plot([up_point[0], down_point[0]], [up_point[1], down_point[1]], color='green', label='Line')
