"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

注意：若 s 和 t 中每个字符出现的次数都相同，则称  s 和 t互为字母异位词。

来源：力扣（LeetCode）
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_a = dict()
        map_b = dict()
        for i in s:
            map_a.setdefault(i, 0)
            map_a[i] += 1

        for j in t:
            map_b.setdefault(j, 0)
            map_b[j] += 1

        return map_a == map_b


solution = Solution()
print(solution.isAnagram("anagram", t="nagaram"))
