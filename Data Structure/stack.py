# 栈
# queue in python
# 使用列表实现

from collections import deque # 通用栈

class queue_Mine():
    def __init__(self):
        self.data = [] # 存储数据
        self.num = 0 # 数据的个数
    
    def isempty(self):
        return self.data == None
    
    def add(self,data):
        item = self.data
        item.append(data)
        self.num += 1
    
    def remove(self):
        item = self.data
        num = self.num
        item.pop(num-1)
    
    def display(self):
        print(self.data)
    
    def length(self):
        item = self.data
        num = len(item)
        return num

# 用内置包实现
s = deque()
# 往里添加元素：
s.append('eat')
s.append('apple')
s.append('sleep')
# 弹出元素：
s.pop()

