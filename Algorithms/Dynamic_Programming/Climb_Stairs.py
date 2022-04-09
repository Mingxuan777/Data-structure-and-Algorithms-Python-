# 动态规划问题
class Solution(object):
    def clibmStairs(self, n):
        if n <= 2:
            return n
        a = 1
        b = 2
        temp = 0
        for i in range(3, n+1):
            temp = a + b
            a = b
            b = temp
        return temp