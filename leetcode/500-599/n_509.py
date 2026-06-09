"""
509. 斐波那契数
"""

class Solution:
    def fib(self, n: int) -> int:

        def f(m):
            if m == 0:
                return 0
            if m == 1:
                return 1
            
            return f(m - 1) + f(m - 2)
        
        def f_1(m):
            if m == 0:
                return 0
            if m == 1:
                return 1
            
            temp = 0
            res = 1
            for _ in range(2, m + 1):
                res, temp = res + temp, res

            return res
        
        def f_2(m):
            a, b = 0, 1
            for _ in range(m):
                a, b = b, a + b
            return a
        
        return f_1(n)