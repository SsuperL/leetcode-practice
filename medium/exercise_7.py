"""
反转整数，整数范围为-2^31<=x<=2^31
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        a = x if x > 0 else -x
        s = ''
        while a >= 10:
            s += str(a % 10)
            a = a//10
        else:
            s += str(a)
        res = int(s)
        if x < 0:
            res = -res
        if res > 2 ** 31-1 or res < -2 ** 31:
            res = 0
        return res


solution = Solution()
print(solution.reverse(1563847412))
