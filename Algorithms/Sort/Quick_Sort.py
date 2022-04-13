# 快速排序
# 使用递归
# 首先指定哨兵Pivot,通过比较-锁定-替换的方法将数组分为比哨兵大和比哨兵小的两个部分，之后递归来实现最终的排序

def quick_sort(lists, i, j):
    if i >= j:
        return list
    pivot = lists[i] # 哨兵
    low = i # 第一个元素
    high = j # 最后一个元素
    while i < j: # 当 i 与 j 还没有相遇时，
        while i < j and lists[j] >= pivot:
            j -= 1
        lists[i] = lists[j] # 互换位置
        # J的位置被锁住了， 给J找一个合适的元素
        while i < j and lists[i] <= pivot: # 接力寻找
            i += 1
        lists[j] = lists[i] # 互换位置

    lists[j] = pivot # 相遇了时候
    quick_sort(lists, low, i-1) # 哨兵左边
    quick_sort(lists, i+1, high) # 哨兵右边
    return lists


lists = [30, 24, 5, 58, 18, 36, 12, 42, 39]
print("排序前的序列为：")
for i in lists:
    print(i, end = " ")
print("\n排序后的序列为：")
for i in quick_sort(lists, 0, len(lists)-1):
    print(i, end=" ")
