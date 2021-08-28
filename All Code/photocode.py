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

class Vertex(object):
    def __init__(self,id) -> None:
        '''点中connectedTo键值对应为:Vertex对象与权重weight'''
        self.id = id
        self.connectedTo = {}
    def addNeighbor(self,neighbor,weights=0) -> None:
        '''增加连接点'''
        self.connectedTo[neighbor] = weights
    def getConnections(self) -> set:
        '''获取连接的点'''
        return self.connectedTo.keys()
    def getId(self):
        '''返回点的ID'''
        return self.id
    def getWeights(self,nbr):
        '''获取边的权重'''
        return self.connectedTo[nbr]
    def __str__(self): 
        '''返回对象描述的字符串'''
        return str(self.id) + ' connectedTo: '+ str([x.id for x in self.connectedTo])

if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    print(g.vertlist)
    g.addEdge(0,1,5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)
    for v in g:
        for w in v.getConnections():
            print("(%s , %s)"%(v.getId(),w.getId()))
