#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque
class Maze():
    def __init__(self, N):
        maze = []
        for _ in range(N):
            maze.append(['#'] * (2 * N + 1))
            maze.append(['#',' '] * N + ['#'])
        maze.append(['#'] * (2 * N + 1))
        self.maze = maze
        self.route = {}

    def __str__(self):
        maze = '\n'.join(''.join(row) for row in self.maze)
        return maze

    def __setitem__(self, key, value):
        #建立相邻房间之间的地图
        start_x, start_y = key[0], key[1].start
        end_x, end_y = key[1].stop, key[2]
        # print(f'{key[0]=} {key[1].start=} {key[1].stop =} {key[2]=} {value=}')
        # print(f'{(start_x, start_y)=} {(end_x, end_y)=}')
        if value == ' ':
            if start_x == end_x:
                for i in range(min(start_y,end_y),min(start_y,end_y)+abs(start_y-end_y)):
                    if (start_x, i) not in self.route:
                        self.route[(start_x, i)] = []
                    if (start_x, i+1) not in self.route:
                        self.route[(start_x, i+1)] = []
                    self.route[(start_x, i)].append((start_x, i+1))
                    self.route[(start_x, i+1)].append((start_x, i))
                    # 改变迷宫图
                    self.maze[(i + 1) * 2][2 * start_x + 1] = ' '
            elif start_y == end_y:
                for i in range(min(start_x,end_x),min(start_x,end_x)+abs(start_x-end_x)):
                    #print(i)
                    if (i, start_y) not in self.route:
                        self.route[(i, start_y)] = []
                    if (i+1, start_y) not in self.route:
                        self.route[(i+1, start_y)] = []
                    self.route[(i, start_y)].append((i+1, start_y))
                    self.route[(i+1, start_y)].append((i, start_y))
                    # 改变迷宫图
                    self.maze[2 * start_y + 1][(i + 1) * 2] = ' '

        elif value == '#':
            if start_x == end_x:
                if abs(start_y - end_y) == 0:
                    return
                elif abs(start_y-end_y) == 1:
                    self.maze[(min(start_y,end_y) + 1) * 2][2 * start_x + 1] = '#'
                    self.route[(start_x, min(start_y,end_y))].remove((start_x, min(start_y,end_y)+1))
                    self.route[(start_x, min(start_y,end_y) + 1)].remove((start_x, min(start_y,end_y)))

                else:
                    for i in range(min(start_y,end_y),min(start_y,end_y)+abs(start_y-end_y)): #i为有变化的量从低到高的房间
                        # 删除值中相应部分
                        #print((start_x, i))
                        #特殊处理首个和最后一个节点
                        if i == min(start_y,end_y):
                            self.route[(start_x, i)].remove((start_x, i+1))
                            # 改变迷宫图
                            self.maze[(i + 1) * 2][2 * start_x + 1] = '#'

                        elif i > min(start_y,end_y) and i < min(start_y,end_y)+abs(start_y-end_y):
                            #print((start_x, i))
                            for key, value in self.route.items():
                                if (start_x, i) in value:
                                    self.route[key].remove((start_x, i))
                            # 改变迷宫图
                            self.maze[(i + 1) * 2][2 * start_x + 1] = '#'

                    for i in range(min(start_y, end_y)+1, min(start_y, end_y) + abs(start_y - end_y)):
                        #删除键
                        del self.route[(start_x, i)]

                for key, value in self.route.items():
                    if value == []:
                        del self.route[key]

            elif start_y == end_y:
                if abs(start_x - end_x) == 0:
                    return
                elif abs(start_x-end_x) == 1:
                    self.maze[2 * start_y + 1][(min(start_x,end_x)+1) * 2] = '#'
                    self.route[(min(start_x,end_x), start_y)].remove((min(start_x,end_x) + 1, start_y))
                    self.route[(min(start_x,end_x) + 1, start_y)].remove((min(start_x,end_x), start_y))
                    pass
                else:
                    for i in range(min(start_x,end_x),min(start_x,end_x)+abs(start_x-end_x)):
                    #print(i)
                    #print((i, start_y))
                    # 改变迷宫图
                        self.maze[2 * start_y + 1][(i + 1) * 2] = '#'

                        if i == min(start_x, end_x):

                            self.route[(i, start_y)].remove((i + 1, start_y))

                        elif i > min(start_x, end_x) and i < min(start_x, end_x) + abs(start_x - end_x):
                            # print((start_x, i))
                            for key, value in self.route.items():
                                if (i, start_y) in value:
                                    self.route[key].remove((i, start_y))

                for i in range(min(start_x,end_x)+1,min(start_x,end_x)+abs(start_x-end_x)):
                    #删除键
                    del self.route[(i, start_y)]

                for key, value in self.route.items():
                    if value == []:
                        del self.route[key]
            #改变迷宫图

    def __getitem__(self, key):
        start_x, start_y = key[0], key[1].start
        end_x, end_y = key[1].stop, key[2]
        #print(f'{(start_x, start_y)=} {(end_x, end_y)=}')
        start = (start_x, start_y)
        end = (end_x, end_y)
        visited = set()
        queue = deque([start])
        visited.add(start)
        while queue:
            node = queue.popleft()
            if node == end:
                return True
            for cell in self.route.get(node, []):
                if cell not in visited:
                    visited.add(cell)
                    queue.append(cell)
        return False
        pass

import sys
exec(sys.stdin.read())