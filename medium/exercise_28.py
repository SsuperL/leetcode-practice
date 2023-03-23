"""
给你两个字符串haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果needle 不是 haystack 的一部分，则返回  -1 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 使用滑动窗口实现
        left, right = 0, len(needle) - 1
        while right < len(haystack):
            if haystack[left : right + 1] == needle:
                return left
            left += 1
            right += 1
        return -1


solution = Solution()
print(solution.strStr(haystack="sadbutsad", needle="sad"))
print(solution.strStr(haystack="leetcode", needle="leeto"))
