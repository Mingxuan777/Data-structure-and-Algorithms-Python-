# 相对于顺序结构的列表而言，节省了数据移位、内存碎片的开支。

class Node:
    def __init__(self, next, val=None):
        self.val = val
        self.next = next

class SLinkList:
  # 分配线性表长度、定义线性表
  def __init__(self, size=7): # 线性表长度
      self.size = size # 线性表长度被定为为7。这个值是固定的
      self.link = [Node((i + 1) % self.size) for i in range(self.size)] # 列表推导式。

  # 线性表清空
  def clearSLL(self):
      self.__init__()

  # 线性表是否为空
  def isEmpty(self):
      return False if self.link[self.size - 1].next else True

  # 查找空位置
  def findEmpty(self):
      ind = self.size
      for i in range(1, self.size - 1):
          if self.link[i].val is None:
              ind = i
              break
      return ind

  # 指定位置插入元素
  def insert(self, ind, ele):
      sua = -1
      # 前一个元素
      pre = self.size - 1
      # 插入元素的位置（第一个空位置）
      insertLoc = self.link[0].next
      # 条件判断
      if ind < 1 or ind >= pre or insertLoc >= self.size:
          return 0
      # 第一个元素的索引
      for i in range(1, self.size - 1):
          index = self.link[pre].next
          if i == ind:
              self.link[pre].next = insertLoc
              # 元素插入
              self.link[insertLoc].val = ele
              self.link[insertLoc].next = index
              # 首位元素
              self.link[0].next = self.findEmpty()
              sua = 1
              break
          if self.link[index].val is None:
              break
          pre = index
      return sua

  # 查找线性表某位置的元素
  def getByIndex(self, ind):
      if ind < 1 or ind >= self.size - 1:
          return -1

      index = self.link[self.size - 1].next
      if index == 0:
          return -1
      for i in range(1, ind):
          index = self.link[index].next

      return self.link[index].val

      # 查找线性表的元素所在位置
  def locateElement(self, ele):
      index = self.link[self.size - 1].next
      ind = -1
      if index == 0:
          return ind
      for i in range(1, self.size - 1):
          if self.link[index].val == ele:
              ind = i
              break
          if self.link[index].val is None:
              break
          index = self.link[index].next
      return ind

      # 删除线性表指定位置的元素
  def deleteElement(self, ind):
      sua = -1
      # 前一个索引
      pre = self.size - 1
      for i in range(1, self.size - 1):
          index = self.link[pre].next
          # 当前位置是个空位置
          if self.link[index].val is None:
              break
          # 已经遍历到第i个位置
          if i == ind:
              self.link[pre].next = self.link[index].next
              self.link[index].val = None
              # 删除元素的游标指向备用链表
              self.link[index].next = self.link[0].next
              # 首位元素
              self.link[0].next = index
              sua = 1
              break
          pre = index
      return sua

      # 按照线性表排序线性表遍历
  def travelLink(self):
      print("*" * 50)
      index = self.link[self.size - 1].next
      while self.link[index].val:
          print(
              f"value = {self.link[index].val} next = {self.link[index].next}"
          )
          index = self.link[index].next
      print("*" * 50)

  # 按照索引遍历
  def traversingByIndex(self):
      print("*" * 50)
      for i in range(self.size):
          print(
              f"index = {i}, value = {self.link[i].val} next = {self.link[i].next}"
          )
      print("*" * 50)

