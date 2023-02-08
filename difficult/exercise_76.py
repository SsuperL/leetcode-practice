"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

 

注意：

对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/minimum-window-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i = 0
        res = ""
        count_dict = dict()
        need_nums = 0
        for item in t:
            if item in count_dict:
                count_dict[item] += 1
            else:
                count_dict[item] = 1

        for j in range(len(s)):
            if s[j] in count_dict:
                count_dict[s[j]] -= 1
                if count_dict[s[j]] == 0:
                    need_nums += 1
                while s[i] not in t or count_dict[s[i]] < 0:
                    if s[i] in t:
                        count_dict[s[i]] += 1
                    i += 1
                if need_nums == len(count_dict):
                    if not res or len(res) > j - i + 1:
                        res = s[i : j + 1]
            else:
                continue

        return res


solution = Solution()
print(solution.minWindow("ADOBECODEBANC", t="ABC"))
print(solution.minWindow("a", "a"))
print(solution.minWindow("aa", "aa"))
