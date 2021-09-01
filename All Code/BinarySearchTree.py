class Node(object):
    def __init__(self,value,lid=None,rid=None) -> None:
        self.value = value
        self.lid = lid
        self.rid = rid
class BST(object): 
    def __init__(self,root=None,data=[]) -> None:
        if(data == []):
            self.root = root
        else:
            self.root = root if root!=None else Node(data[0])
            for i in range(0 if root!=None else 1,len(data)-1):
                self.insert(root,data[i])

    def insert(self,root,value):
        '''插入某节点'''
        if root==None:
            root = Node(value)
            return
        if value == root.value:return
        elif(value < root.value):
            self.insert(root.lid,value)
        else:
            self.insert(root.rid,value)
    def find(self,root,value):
        '''寻找节点'''
        while(root!=None):
            if(root.value==value):
                return True
            elif(root.value<value):
                root = root.lid
            else:
                root = root.rid
        return False
                
            