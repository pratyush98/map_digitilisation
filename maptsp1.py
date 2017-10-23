import sys, pygame
import numpy as np
from numpy import random
import cv2
from collections import defaultdict
pygame.init()
black = 0, 0, 0
size = width, height = 1000,600
screen = pygame.display.set_mode(size)
pointx=0;pointy=0
c=0
x_=[]
y_=[]
name_=[]
ho=0
lol=0
lol2=''
mapedge1=[]
mapedge2=[]
weight=[]
img1=pygame.image.load("mapiitr.png")
#dfs traversal
background=img1.get_rect()
def find_shortest_path(graph, start, end, weighted, path=[],weight1=0):
    path = path + [start]
    if start == end:
        return path
    shortest = None
    shortestw=None
    for node,weigh in zip(graph[start],weighted[start]):
        if node not in path:
            weight1 = weight1 + weigh
            newpath = find_shortest_path(graph, node, end,weighted, path,weight1)
            if newpath:
                if not shortestw or shortestw > weight1:
                    shortest = newpath
                    shortestw=weight1
            weight1 = weight1 - weigh
    return shortest

#graph structure..

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print mapedge1
            print mapedge2
            print weight
            g = Graph()
            for po in name_:
                g.add_vertex(po)
            for ed1,ed2,wei in zip(mapedge1,mapedge2,weight):
                g.add_edge(ed1,ed2,wei)
            dictf={}
            path=[]
            weighted={}
            for v in g:
                arr=[]
                arr1 = []
                vid = v.get_id()
                for w in v.get_connections():
                    wid = w.get_id()
                    arr.append(wid)
                    arr1.append(v.get_weight(w))
                dictf[vid]=arr
                weighted[vid]=arr1
            print dictf
            start=raw_input("where is the starting point??")
            end=raw_input("where is the ending point??")
            print find_shortest_path(dictf, start, end,weighted)
            sys.exit()
    if (pygame.mouse.get_pressed()[0]):
     pos = pygame.mouse.get_pos()
     for i, j,nam in zip(x_, y_,name_):
        if((np.abs(i-pos[0])<10)and(np.abs(j-pos[1])<10)):
            if c==1:
             pygame.draw.line(screen, 0x00ff00, (pointx, pointy),(i,j), 5)
             if mapedge1[mapedge1.__len__()-1]!=nam:
              mapedge1.append(nam)
              mapedge2.append( name_[name_.__len__() - 1])
              weight.append(np.sqrt((pointx-i)*(pointx-i)+(pointy-j)*(pointy-j)))
              print nam
            ho=1
            if c==0:
                lol=1
                lol2=nam
            pointx=i
            pointy=j
            c=1
            break
    if ho==1:
        ho=0
        continue
    if(pygame.mouse.get_pressed()[0]):
        pos=pygame.mouse.get_pos()
        if pointx!=pos[0]and pointy!=pos[1]:
         if c==1:
          pygame.draw.line(screen, 0xff0000,(pointx,pointy),pos,5)
         str1 = raw_input("input place name..")
         name_.append(str1)
         if c==1:
          if lol==1:
           mapedge1.append(lol2)
           mapedge2.append(name_[name_.__len__() - 1])
           lol=0
          else:
           mapedge1.append(name_[name_.__len__()-2])
           mapedge2.append(name_[name_.__len__()-1])
          weight.append(np.sqrt((pos[0]-pointx)**2+(pos[1]-pointy)**2))
         c=1
         pointx = pos[0]
         pointy = pos[1]
         x_.append(pointx)
         y_.append(pointy)
    if(pygame.mouse.get_pressed()[2]):
        c=0
    screen.blit(img1, (0, 0))
    pygame.display.flip()