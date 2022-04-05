#binary_tree in python

#定义单个的树节点
class node():
    def __init__(self,data = None):
        self.data = data # 存储数据
        self.right_child = None # 右侧子节点
        self.left_child = None # 左侧子节点
        self.parent = None # 母节点

class binary_tree():
    def __init__(self):
        self.root = None
    
    #add numbers to binary_tree
    def append(self,data):
        if self.root == None:
            self.root = node(data) # 如果树是空的，那么这是第一个节点
        else:
            self._insert(self.root,data)

    def _insert(self,cur_node,data):
        if cur_node.data > data: # 当前节点的数字比添加的数字大
            if cur_node.left_child == None:
                cur_node.left_child = node(data) # 添加数字
                cur_node.left_child.parent = cur_node # 链接母节点
            else:
                self._insert(cur_node.left_child,data) # 遍历左侧分支，直到找到空节点
        
        elif cur_node.data < data: # 当前节点的数字比添加的数字小
            if cur_node.right_child == None:
                cur_node.right_child = node(data) # 添加数字
                cur_node.right_child.parent = cur_node # 链接母节点
            else:
                self._insert(cur_node.right_child,data) # 遍历右侧分支，直到找到空节点
        
        else:
            print('data is already in the list!')
        
    #print the tree
    def print_tree(self):
        if self.root == None:
            print('no numbers in the tree')
            return
        elif self.root != None:
            self._print_tree(self.root)
            self._rlr_print_tree(self.root)
            self._lrr_print_tree(self.root)
    
    #print binary_tree(left-root-right)
    def _print_tree(self,cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print(cur_node.data)
            self._print_tree(cur_node.right_child)

    #print binary_tree(root,left,right)
    def _rlr_print_tree(self,cur_node):
        if cur_node != None:
            print(cur_node.data)
            self._rlr_print_tree(cur_node.left_child)
            self._rlr_print_tree(cur_node.right_child)

    
    #print binary tree(left-right-root)
    def _lrr_print_tree(self,cur_node):
        if cur_node != None:
            self._lrr_print_tree(cur_node.left_child)
            self._lrr_print_tree(cur_node.right_child)
            print(cur_node.data)


    
    #find number in binary-tree
    def find(self,data):
        if self.root == None:
            print('no data in the list')
            return 
        
        elif self.root != None:
            self._find(self.root,data)
    
    def _find(self,cur_node,data):
        if cur_node != None:
            self._find(cur_node.left_child,data)
            if data == cur_node.data:
                print(str(data) + ' ' + 'has found!')
            self._find(cur_node.right_child,data)
    
    #get depth of the tree
    def get_depth(self):
        if self.root == None:
            print('its an empty list')
            return False
        elif self.root != None:
            depth = self._get_depth(self.root,0)
            print('depth is '+str(depth))
            
    
    def _get_depth(self,cur_node,cur_height):
        if cur_node == None: 
            return cur_height
        left_height = self._get_depth(cur_node.left_child,cur_height+1)
        right_height = self._get_depth(cur_node.right_child,cur_height+1)
        return max(left_height,right_height)
    
    #delete number
    def delet(self,data):
        if self.root == None:
            return
        
        else:
            self._delet(self.root, data)
    
    def _delet(self, cur_node, data):
        pass