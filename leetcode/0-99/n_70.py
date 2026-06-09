"""
70. 爬楼梯
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        
        def f(m):
            if m == 1:
                return 1
            elif m == 2:
                return 2
            return f(m - 1) + f(m - 2)
        
        def f_1(m):
            if m == 1:
                return 1
            elif m == 2:
                return 2
            
            temp = 1
            res = 2
            for i in range(3, m + 1):
                res, temp = res + temp, res

            return res

        
        return f_1(n)