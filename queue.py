#queue in python
class queue():
    def __init__(self):
        self.data = []
        self.num = 0
    
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