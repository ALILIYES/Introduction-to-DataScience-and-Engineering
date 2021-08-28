class TreeNode(object):
    '''树节点'''
    def __init__(self,value,lid=None,rid=None) -> None:
        self.value = value
        self.lid = lid
        self.rid = rid
class BinaryTree(object):
    '''二叉树'''
    def __init__(self,root=None) -> None:
        self.root = root
    def is_empty(self) -> bool:
        return self.root==None
    def left_child(self) -> TreeNode:
        return self.left_child
    def right_child(self) -> TreeNode:
        return self.right_child

def is_equal(root1:TreeNode,root2:TreeNode):
    tmp1 = list(level_order(root1))
    tmp2 = list(level_order(root2))
    return tmp1==tmp2

def cnt_node(root:TreeNode) ->int:
    '''求树中所有节点个数'''
    if root == None:
        return 0
    return 1+cnt_node(root.lid)+cnt_node(root.rid)
def sum_Treevalue(root:TreeNode) -> int:
    '''求树中所有节点和'''
    if root == None:
        return 0
    return root.value+sum_Treevalue(root.lid)+sum_Treevalue(root.rid)
def preorder(root:TreeNode) -> None:
    '''先序遍历'''
    if root==None:
        return 
    print(root.value)
    preorder(root.lid)
    preorder(root.rid)
def midorder(root:TreeNode) -> None:
    '''中序遍历'''
    if root==None:
        return 
    preorder(root.lid)
    print(root.value)
    preorder(root.rid)
def aftorder(root:TreeNode) -> None:
    '''后序遍历'''
    if root==None:
        return 
    preorder(root.lid)
    preorder(root.rid)
    print(root.value)

from Queue import Queue
def level_order(root:TreeNode) -> None:
    '''层序遍历'''
    if root == None:return 
    qu = Queue()
    qu.push(root)
    while qu.is_empty() != True:
        tmp = qu.front()
        qu.pop()
        if tmp == None:continue
        qu.push(tmp.lid)
        qu.push(tmp.rid)
        yield tmp.value
    
