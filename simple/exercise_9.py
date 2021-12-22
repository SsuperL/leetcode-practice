"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。


进阶：你能不将整数转为字符串来解决这个问题吗？

通过次数845,036提交次数1,454,057

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 不将x转换为字符串的方式
        if x < 0:
            return False
        if x == 0:
            return True
        tmp1 = x
        tmp = 0
        while x != 0:
            tmp = tmp*10+x % 10
            x = x//10
        return tmp1 == tmp
        # x = str(x)
        # return x == x[::-1]


solution = Solution()
print(solution.isPalindrome(121))
