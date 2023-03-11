"""
给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符。

如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/reverse-string-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(s_list):
            """
            Do not return anything, modify s in-place instead.
            """
            left, right = 0,len(s_list)-1

            while left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
            return s_list

        # 将字符串转换为数组
        s_list = list(s)
        # 用一个变量统计反转数组的起始位置
        left = 0
        l=len(s_list)-1
        # 以 2k 步长循环
        while left < l:
            # s[0:999] -> 'abc' 超出长度的部分仅返回数组所有元素
            s_list[left:left+k] = reverse(s_list)
            left+=2*k
        # for _ in range(0,l,2*k):
        #     # 如果剩余元素个数小于 2k，退出循环
        #     if l-left+1<2*k:
        #         break
        #     reverse(s_list,left,k)
        #     # 变量 left 以 2k 递增
        #     left +=2*k

        # print(s_list[left:])
        # remain = len(s_list[left:])
        # print(remain)
        # # 剩余元素大于等于 k 小于 2k，则反转剩余部分的前 k 个元素
        # if k<=remain<2*k:
        #     reverse(s_list,left,k)
        # # 剩余部分小于 k ，则全部反转
        # if remain<k:
        #     reverse(s_list,left,remain)
        return "".join(s_list)
    
solution = Solution()
# "bacdfeg"
print(solution.reverseStr(s = "abcdefg", k = 2))
# "bacd"
print(solution.reverseStr("abcd",4))
print(solution.reverseStr("abcd",2))
# "gfedcba"
print(solution.reverseStr(s = "abcdefg", k = 8))