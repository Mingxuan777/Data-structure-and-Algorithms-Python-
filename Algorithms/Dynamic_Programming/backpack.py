# 0-1 Knapsack Problem 0-1背包问题

weight = [4, 5, 6, 2, 2]
value = [6, 4, 5, 3, 6]
CAPACITY = 8
NUM = len(weight)

def knapsack_MATRIX():
    optimal = [[0 for x in range(CAPACITY + 1)] for x in range(NUM + 1)] # 使用列表推倒式构建2维列表
    for i in range(1, NUM + 1): # 先索引列，后索引行
        for j in range(1, CAPACITY + 1):
            if j >= weight[i-1]: # 能不能装进去，j比当前能装的大，装
                optimal[i][j] = max(optimal[i - 1][j], optimal[i - 1][j - weight[i - 1]] + value[i - 1]) # 上一个单元格的值与(当前单元格值和剩下重量带来最大值的和)
            else:
                optimal[i][j] = optimal[i - 1][j]
            print(optimal[i][j], end=" ")
        print("\n", end="")
    print("\nthe optimal solution is:" + str(optimal[NUM][CAPACITY]) + "\n")


def knapsack():
    optimal = [0 for x in range(CAPACITY + 1)]
    for i in range(0, NUM):
        for j in range(CAPACITY, weight[i] - 1, -1):
            optimal[j] = max(optimal[j], optimal[j - weight[i]] + value[i])
            print(optimal[j], end=" ")
        print("\n", end="")
    print("\nthe optimal solution is:" + str(optimal[CAPACITY]) + "\n")


if __name__ == '__main__':
    print("二维数组\n________")
    knapsack_MATRIX()
    print("一维数组\n________")
    knapsack()
