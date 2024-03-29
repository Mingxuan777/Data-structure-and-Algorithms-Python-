# 单向列表：
# 对于每个节点的定义，有储存数据的部分，前节点与后节点组成
# 主要的方法有 判断是否位空，列表长度，遍历，添加，以及查找。

# 单个节点的定义
class Node():
    def __init__(self,data = None):
        self.data = data # 存储数据
        self.next = None # 存储节点

# 存储数据与操作
class Linked_list():
    def __init__(self):
        self.head = Node()
    
    # 添加数据
    def Append(self, data):
        cur = self.head
        new_node = Node(data)
        while cur.next != None: # 向前遍历
            cur = cur.next
        cur.data = data
        cur.next = new_node

    # 打印数据
    def display(self):
        # 新建列表，将每一个节点的数字添加进去
        cur = self.head
        item = []
        while cur.next != None:
            item.append(cur.data)
            cur = cur.next
        print(item)
    
    # 返回长度
    def length(self):
        # 设置total = 0，迭代列表，并且给total 逐次加1
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
    
    # 按位置删除
    def remove(self, index):
        cur = self.head
        pre = self.head
        number = 0 # 遍历位置
        while cur:
            if index >= self.length() or index < 0:
                print('error')
                return False
            else:
                if number == index:
                    pre.next = cur.next # 前一个节点的指针指向下一个节点
                    print('deleted!')
                    return True
                else:
                    number += 1
                    pre = cur
                    cur = cur.next
        return
    
    # 按元素删除
    def removedata(self, data):
        cur = self.head
        pre = self.head
        while cur.next != None:
            if cur.data == data:
                pre.next = cur.next # 变换指针， pre.next = cur.next 而不是 cur
                print('data removed')
                return
            else:
                pre = cur
                cur = cur.next
        print('It is a empty list')
    
    # 搜寻元素
    def find(self, data):
        cur = self.head
        while cur.next != None:
            if cur.data == data:
                print('founded')
                return True
            else:
                cur = cur.next
        print('list is empty!')
    
    # 搜寻，按元素位置
    def insert(self, index, data):
        new_node = Node(data)
        cur = self.head
        pre = self.head
        number = 0
        while cur:
            if index >= self.length() or index < 0:
                print('Error')
                return False
            else:
                if number == index:
                    pre.next = new_node
                    new_node.next = cur
                    print('added')
                    return True
                else:
                    number += 1
                    pre = cur
                    cur = cur.next
        self.Append(data)
    
    # 返回引索
    def getindex(self, data):
        cur = self.head
        num = 0
        while cur:
            if cur.data == data:
                print(num)
                return True
            else:
                cur = cur.next
                num += 1
        print('not in the database')
        return False