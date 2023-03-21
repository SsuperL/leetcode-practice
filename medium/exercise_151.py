"""
给你一个字符串 s ，请你反转字符串中 单词 的顺序。

单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。

返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。

注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/reverse-words-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        left, right = 0, len(s_list) - 1
        while left <= right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

        return " ".join(s_list)


solution = Solution()
print(solution.reverseWords("    example dd"))
