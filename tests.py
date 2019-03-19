# imports random value for random points and and imports plotting library
import matplotlib.pyplot as plt
import random

# public vars
grid_width = 10
grid_height = 10

max_lvls = 4

num_points = 15

pts = []


# class of a point, has a simple x value and y value
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.z = z

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def __repr__(self):
        return self.__str__()


# Octree structure itself
class Octree:
    def __init__(self, root, max_lvl):
        self.root = root
        self.max_lvl = max_lvl
        root.set_children()


# group structure, essentially just an array of points
class Group:
    def __init__(self, pts, lvl):
        self.pts = pts
        if lvl >= max_lvls:
            self.isLeaf = True
        else:
            self.isLeaf = False
        self.level = lvl

        self.quad_i = []
        self.quad_ii = []
        self.quad_iii = []
        self.quad_iv = []

        self.g1 = None
        self.g2 = None
        self.g3 = None
        self.g4 = None

    # finds the children in each standard quadrant
    def set_children(self):
        new_width = grid_width/(self.level*2)
        new_height = grid_height/(self.level*2)

        for point in self.pts:
            if(point.x > new_width) and (point.y > new_height):
                self.quad_i.append(point)
            elif(point.x <= new_width) and (point.y > new_height):
                self.quad_ii.append(point)
            elif(point.x <= new_width) and (point.y <= new_height):
                self.quad_iii.append(point)
            elif(point.x > new_width) and (point.y <= new_height):
                self.quad_iv.append(point)

        self.print_childs()

        # stop statement
        if self.isLeaf is False:
            self.g1 = Group(self.quad_i, self.level+1)
            self.g2 = Group(self.quad_ii, self.level + 1)
            self.g3 = Group(self.quad_iii, self.level + 1)
            self.g4 = Group(self.quad_iv, self.level + 1)

    def print_childs(self):

        print(self.level)

        print('quad 1')
        print(self.quad_i)
        print('quad 2')
        print(self.quad_ii)
        print('quad 3')
        print(self.quad_iii)
        print('quad 4')
        print(self.quad_iv)
        print(' ')


# generates random points
def point_gen():
    for n in range(num_points + 1):
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        pts.append(Point(x, y))


point_gen()

for pt in pts:
    plt.plot(pt.x, pt.y, 'o')

rt = Group(pts, 1)

octy = Octree(rt, max_lvls)

# point plotting
plt.axis([0, 10, 0, 10])
plt.show()


