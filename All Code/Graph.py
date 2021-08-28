from Vertex import *
class Graph(object):
    def __init__(self) -> None:
        '''图中的vertlist键值对应为:点key与Vertex对象'''
        self.vertlist = {}
        self.vertnum = 0
    def addVertex(self,key) -> Vertex:
        '''给图中增加点'''
        self.vertnum = self.vertnum + 1
        newVert = Vertex(key)
        self.vertlist[key] = newVert
        return newVert
    def getVertex(self,key):
        '''获取此点连接的所有边'''
        if key in self.vertlist:
            return self.vertlist[key]
        else:
            return None
    def __contains__(self,key):
        '''是否包含此点'''
        return key in self.vertlist
    def addEdge(self,start,end,weight=0):
        '''在图中加入新边'''
        if start not in self.vertlist:
            newVect = self.addVertex(self,start)
        if end not in self.vertlist:
            newVect = self.addVertex(self,end)
        self.vertlist[start].addNeighbor(self.vertlist[end],weight)
    def getVertices(self):
        '''获取图中所有顶点'''
        return self.vertlist.keys()
    def __iter__(self):
        return iter(self.vertlist.values())