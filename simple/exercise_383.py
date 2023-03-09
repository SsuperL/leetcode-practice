"""
给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。

如果可以，返回 true ；否则返回 false 。

来源：力扣（LeetCode）
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # map_a = dict()
        # map_b = dict()
        # for i in ransomNote:
        #     map_a.setdefault(i, 0)
        #     map_a[i] += 1
        #
        # for j in magazine:
        #     map_b.setdefault(j, 0)
        #     map_b[j] += 1
        # for i in ransomNote:
        #     if i not in magazine:
        #         return False
        #     if map_a[i] > map_b[i]:
        #         return False

        # 方法二，使用数组进行映射操作题目
        # 题中限定字符均是小写字母
        arr = [0] * 26
        for i in magazine:
            arr[ord(i) - ord("a")] += 1

        for j in ransomNote:
            if arr[ord(j) - ord("a")] == 0:
                return False
            arr[ord(j) - ord("a")] -= 1

        return True


# solution = Solution()
# print(solution.canConstruct("a", "b"))

a = [{0: 1}, {1: 2}, {2: 3}, {3: 4}]
for idx, item in enumerate(a):
    item[idx] += 1

for item in a:
    print(item)
