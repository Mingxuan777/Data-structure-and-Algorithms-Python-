# 哈希表Python实现。余数法构造散列函数，"+1"法进行rehash

class HashTable:
    def __init__(self):
        self.size = 11 # 定义Hash表的长度
        self.slots = [None] * self.size # 初始化，全为None
        self.data = [None] * self.size

    def hashfunction(self, key, size): # Hash函数，取余获得index
        return key%size

    def rehash(self, oldhash, size): # +1 来rehash
        return (oldhash + 1) % size

    def put(self, key, data): # 添入元素
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None: # 最理想的情况：如果slot是空的，则放入index和value
            self.slots[hashvalue] = key
            self.data[hashvalue] = data

        # 否则进行判断
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data # 用新值代替旧值
            else:
                nextslot = self.rehash(hashvalue, len(self.slots)) # 找到下一个空槽
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots)) # 重新hash，相当于搜寻下一个可用的位置

                if self.slots[nextslot] == None: # 搜寻到空槽：添加key和value
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data # 用新值替换旧值

    def get(self, key): # 获取元素
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key: # key相等时，说明找到了所要找的value
                found = True
                data = self.data[position]
            else: # 否则向下hash并搜寻
                postion = self.rehash(position, len(self.slots))
            if position == startslot:
                stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
