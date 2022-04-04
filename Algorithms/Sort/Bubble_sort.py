# 冒泡排序
# 两个for，算法复杂度O(n2)
# 通过对比相邻两个数的大小，将大数逐渐向右推

import time

def bubbleSprt(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
