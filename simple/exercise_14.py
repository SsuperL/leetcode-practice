"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
"""
from typing import List
from collections import Counter


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        # 使用zip的解压特性
        # [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'i', 'a'), ('w', 'g', 't'), ('e', 'h', 't'), ('r', 't', 'e')]
        for i in zip(*strs):
            if len(set(i)) == 1:
                res += i[0]
            else:
                return res
        return res


solution = Solution()
print(solution.longestCommonPrefix([""]))
