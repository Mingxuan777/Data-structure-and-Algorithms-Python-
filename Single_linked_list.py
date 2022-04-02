#linked_list in python
class Node():
    def __init__(self,data = None):
        self.data = data # 存储数据
        self.next = None # 存储节点
    
class Linked_list():
    def __init__(self):
        self.head = Node()
    
    # 添加数据
    def Append(self,data):
        cur = self.head
        new_node = Node(data)
        while cur.next != None:
            cur = cur.next
        cur.data = data
        cur.next = new_node

    # 打印数据
    def display(self):
        cur = self.head
        item = []
        while cur.next != None:
            item.append(cur.data)
            cur = cur.next
        print(item)
    
    # 返回长度
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
    
    # 按位置删除
    def remove(self,index):
        cur = self.head
        pre = self.head
        number = 0
        while cur:
            if index >= self.length() or index < 0:
                print('error')
                return False
            else:
                if number == index:
                    pre.next = cur.next
                    print('deleted!')
                    return True
                else:
                    number += 1
                    pre = cur
                    cur = cur.next
        return
    
    # 按元素删除
    def removedata(self,data):
        cur = self.head
        pre = self.head
        while cur.next != None:
            if cur.data == data:
                pre.next = cur.next
                print('data removed')
                return
            else:
                pre = cur
                cur = cur.next
        print('It is a empty list')
    
    # 搜寻元素
    def find(self,data):
        cur = self.head
        while cur.next != None:
            if cur.data == data:
                print('founded')
                return True
            else:
                cur = cur.next
        print('list is empty!')
    
    # 搜寻，按元素位置
    def insert(self,index,data):
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
    def getindex(self,data):
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