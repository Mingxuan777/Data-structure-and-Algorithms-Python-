# 归并排序， 使用递归
# 如何理解？递归先探测做分支直到最小的颗粒，之后开始排序，一步步向上。
# 应该是运用了两次递归。依次是left/right 的搜索，另外一是排好序的元素

def mergesort(seq): # returns sorted list
    """归并排序"""
    if len(seq) <= 1: # 递归终止条件
        return seq
    mid = int(len(seq) / 2)  # 将列表分成更小的两个列表，递归处理
    # 分别对左右两个列表进行处理，分别返回两个排序好的列表
    left = mergesort(seq[:mid])
    right = mergesort(seq[mid:])
    # 对排序好的两个列表合并，产生一个新的排序好的列表

    result = []  # 新的已排序好的列表
    i = 0  # 下标
    j = 0
    # 对两个列表中的元素 两两对比。
    # 将最小的元素，放到result中，并对当前列表下标加1
    while i < len(left) and j < len(right): # 比较大小
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # 这里应该是把最后一个元素加上去了。
    result += left[i:] # 注意i:
    result += right[j:] # 注意是j:
    return result

seq = [5,3,0,2,7,6,1,4]
result = mergesort(seq)
print(result)
