class Stack(object):
    def __init__(self):
        self.__items = []
    # push(item)
    def push(self,item):
        self.__items.append(item)
    # pop(item)
    def pop(self):
        self.__items.pop()
    # peek() 返回栈顶元素
    def peek(self):
        return self.__items[self.size()-1]
    # is_empty() 判断栈是否为空
    def is_empty(self):
        return self.__items == []
    # size() 返回栈元素个数
    def size(self):
        return len(self.__items)
    # clear() 清空栈
    def clear(self):
        self.__items = []


if __name__ == '__main__':
    st = Stack()
    st.push(2)
    st.push(3)
    st.push(4)
    st.pop()
    print(st.peek())
    st.clear()
    # st.push(5)
    print(st.is_empty())
