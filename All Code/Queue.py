class Queue(object):
    def __init__(self) -> None:
        self.__items = []
    def push(self,item) ->None:
        '''入队'''
        self.__items.append(item)
    def pop(self) -> None:
        '''出队'''
        self.__items.pop(0)
    def size(self) -> int:
        '''队列长度'''
        return len(self.__items)
    def is_empty(self) -> bool:
        '''判断是否为空'''
        return self.__items == []
    def front(self):
        '''队首元素'''
        return self.__items[0]
    def behind(self):
        '''队尾元素'''
        return self.__items[self.size()-1]
    def clear(self):
        '''清空队列'''
        self.__items = []
    