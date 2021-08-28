from BinaryTree import *

def fill_tree(root:TreeNode,start,gap,depth):
    '''按照顺序填充树'''
    if depth == 0:return
    root.lid = TreeNode(start)
    root.rid = TreeNode(start)
    fill_tree(root.lid,start+gap,gap,depth-1)
    fill_tree(root.rid,start+gap,gap,depth-1)

if __name__ == '__main__':
    Tree1 = BinaryTree(TreeNode(1))
    Tree2 = BinaryTree(TreeNode(1))
    fill_tree(Tree1.root,2,1,3)
    fill_tree(Tree2.root,2,1,4)
    # for i in level_order(Tree1.root):print(i)
    # for i in level_order(Tree2.root):print(i)
    print(is_equal(Tree1.root,Tree2.root))