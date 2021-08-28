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