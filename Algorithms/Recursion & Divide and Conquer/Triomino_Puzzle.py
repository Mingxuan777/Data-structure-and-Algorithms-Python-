# 棋盘覆盖问题
# 递归，分治
# 在棋盘覆盖问题中，要用四种L型骨牌覆盖给定的特殊棋盘上除方格以外的所有方格。且任何两个L型骨牌不得已重叠。
# 对于边长为2的n次方的正方形，可以分为4个2的n-1次方个正方形。假设除了那个有特殊方块的子棋盘之外，其余棋盘也为特殊子棋盘，通过将剩余子棋盘拼接称一个L，解决。
# 特殊方格的横坐标，纵坐标，左上角横坐标，纵坐标， 棋盘边的长度

# tr 棋盘左上角的行号
# tc 棋盘左上角方格的列号
# pr 特殊方格的行号
# pc 特殊方格的列号
# size 棋盘规模

def chess(tr, tc, pr, pc, size):
    global mark
    global table
    mark += 1
    count = mark
    if size == 1:
        return
    half = int(size / 2) # half实际上是引索

    # 左上角子棋盘
    if pr < tr + half and pc < tc + half:  # 判断是否是特殊棋盘
        chess(tr, tc, pr, pc, half) # 划分
    else: # 如果不是，转化为特殊棋盘
        table[tr + half - 1][tc + half - 1] = count # 覆盖右下角
        chess(tr, tc, tr + half - 1, tc + half - 1, half)

    # 右上角子棋盘
    if pr < tr + half and pc >= tc + half: # 判断是否是特殊棋盘
        chess(tr, tc + half, pr, pc, half)
    else:
        table[tr + half - 1][tc + half] = count # 覆盖左下角
        chess(tr, tc + half, tr + half - 1, tc + half, half)

    # 左下角子棋盘
    if pr >= tr + half and pc < tc+half: # 判断是否是特殊棋盘
        chess(tr + half, tc, pr, pc, half)
    else:
        table[tr + half][tc + half - 1] = count # 覆盖右上角
        chess(tr + half, tc, tr + half, tc + half - 1, half)

    # 右下角子棋盘
    if pr >= tr + half and pc >= tc + half: # 判断是否是特殊棋盘
        chess(tr + half, tc + half, pr, pc, half)
    else:
        table[tr + half][tc + half] = count # 覆盖左上角
        chess(tr + half, tc + half, tr + half, tc + half, half)

def show(table):
    n = len(table)
    for i in range(n):
        for j in range(n):
            print(table[i][j], end = ' ')
        print('')

mark = 0
n = 8
table = [[-1 for x in range(n)] for y in range(n)]
chess(0, 0, 2, 2, n)
show(table)