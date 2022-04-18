# 插入排序
# 提出来一个元素，插入到它合适的位置上
# 在搜索的时候会有两个元素重复，这个问题会在找到位置后元素被放入消除。
# 一个for循环
# 如果a[n]比a[n+1]大，交换两数，反之则a[n+1]=a[n]
# 相比冒泡循环，效率提升

import time

def insertionSort(arr):
    for i in range(1, len(arr)):
        # 增加的是i
        key = arr[i]
        j = i - 1 # j 是 arr[i] 的前一个元素
        while j >= 0 and key < arr[j]: # 扫描
            arr[j + 1] = arr[j] # 调整大小关系
            j -= 1
        arr[j + 1] = key # 插入元素

q = [15, 22, 17, 36, 21]
insertionSort(q)
print(q)
