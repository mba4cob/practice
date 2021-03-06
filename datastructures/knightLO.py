#!/bin/python3

import math
import os
import random
import re
import sys
import cProfile

adj = []
size = 0

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.moves = 0

    def is_valid(self):
        return self.moves == 0

def neighbours(point, moves):
    ns = []
    (i, j) = moves
    (x, y) = point.x, point.y

    neighbours1 = [(x+i, y+j), (x+i, y-j), (x-i, y+j), (x-i, y-j)]



    valid = filter(lambda v: v[0]>= 0 and v[0]<size and v[1]>=0 and v[1]<size, neighbours1)

    # print("valid : ", valid)

    cord = []
    for (v1, v2) in valid:
        cord.append(Point(v1, v2))

    if not i == j:
        neighbours2 = [(x+j, y+i), (x+j, y-i), (x-j, y+i), (x-j, y-i)]
        valid = [ (v1, v2) for (v1, v2) in neighbours2 if v1 >= 0 and v1 < size and v2 >= 0 and v2 < size ]
        for (v1, v2) in valid:
            cord.append(Point(v1, v2))
  
    for cordinate in cord:
        if cordinate.is_valid(): ns.append(cordinate)

    # for cord in ns:
    #   print("cord :", cord.x, cord.y)

    return ns

def reset_adj():
    global adj
    adj = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(0)
        adj.append(row)

def knight_count(x, y):

    print("inside knight_count :", x, y)
    start = Point(0, 0)
    #ns = neighbours(start, (x, y))
    reset_adj()

    q = []
    q.append(start)
    while(q):
        cord = q.pop(0)
        if cord.x == size-1 and cord.y == size-1:
            print("moves :", cord.moves)
            return cord.moves
        print("cord :", cord.x, cord.y)
        ns = neighbours(cord, (x, y))
        #print("ns len :", len(ns))
        for node in ns:
            if adj[node.x][node.y] == 0:
                node.moves = cord.moves+1
                q.append(node)
        adj[cord.x][cord.y] = 1

    return -1


# Complete the knightlOnAChessboard function below.
def knightlOnAChessboard(n):
    global size
    size = n

    count_mat = []

    for i in range(n-1):
        row = []
        for j in range(n-1):
            row.append(0)
        count_mat.append(row)

    #print("count_mat :", count_mat)
    

    for i in range(n-1):
        for j in range(i, n-1):
            count = knight_count(i+1, j+1)
            count_mat[i][j] = count
            count_mat[j][i] = count
            #print("count :", count)

    return count_mat
            


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input())


    cProfile.run("knightlOnAChessboard(5)")
    # result = knightlOnAChessboard(5)

    # print("result :", result)

    # fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    # fptr.write('\n')

    # fptr.close()
