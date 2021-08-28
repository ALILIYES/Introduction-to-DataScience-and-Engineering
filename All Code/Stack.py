class Stack(object):
    def __init__(self):
        self.__items = []
    def push(self,item):
        '''入栈'''
        self.__items.append(item)
    def pop(self):
        '''出栈'''
        self.__items.pop()
    def peek(self):
        '''返回栈顶元素'''
        return self.__items[self.size()-1]
    def is_empty(self):
        '''判断栈是否为空'''
        return self.__items == []
    def size(self):
        '''返回栈元素个数'''
        return len(self.__items)
    def clear(self):
        '''清空栈'''
        self.__items = []
