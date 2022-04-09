# 使用递归实现sum函数

def Mysum(sums, num):
    '''使用递归实现sum函数'''
    # 基线条件
    global sum_final

    if len(num) == 1 and sum(num) == num[-1]:
        sum_final = sums + num[0]
        return

    sums = sums + num.pop(0)
    Mysum(sums, num) # 递归条件

Mysum(0, [1,2,3,4,5,6])
print(sum_final)
