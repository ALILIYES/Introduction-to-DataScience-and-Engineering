
class Node(object):
    '''节点'''
    def __init__(self,value,id=None) -> None:
        self.value = value
        self.next = id

class SingleLink(object):
    '''单链表'''
    def __init__(self,node=None) -> None:
        #定义头节点
        self._head = node
    def is_empty(self) -> bool:
        #判断是否为空
        return self._head==None
    def length(self) -> int:
        #判断链表长度
        res = 0
        cur = self._head
        while cur != None:
            res+=1
            cur = cur.next
        return res
    def travel(self) -> None:
        #遍历链表
        cur = self._head
        while cur != None:
            print(str(cur.value)+" ")
            cur = cur.next
    def add(self,value) -> None:
        #链表头部增加节点
        cur = Node(value,self._head)
        self._head = cur
    def append(self,value) -> None:
        #链表尾部增加节点
        cur = Node(value)
        if self.is_empty():
            self._head = cur
        else:
            end = self._head
            while end.next != None:
                end = end.next
            end.next = cur
    def insert(self,pos,value) -> None:
        #在pos位置插入节点
        if pos <= 0:
            self.add(value)
        elif pos > self.length()-1:
            self.append(value)
        else:
            newNode = Node(value)
            cur = self._head
            for i in range(1,pos):
                cur = cur.next
            newNode.next = cur.next
            cur.next = newNode
    def remove(self,value) -> bool:
        #移除某个节点
        cur = self._head
        if(cur.value == value):
            self._head = cur.next
            return True
        pre = self._head
        cur = cur.next
        while cur.value != value:
            cur = cur.next
            pre = pre.next
        if cur.value == None:return False
        pre.next = cur.next
        return True
    def search(self,value) -> bool:
        #遍历链表
        cur = self._head
        while cur != None:
            if cur.value == value:
                return True
        return False

if __name__ == "__main__":
    ll = SingleLink()
    print(ll.is_empty())
    print(ll.length())
    ll.append(3)
    ll.add(999)
    ll.insert(-3, 110)
    ll.insert(99, 111)
    print(ll.is_empty())
    print(ll.length())
    ll.travel()
    ll.remove(111)
    ll.travel()