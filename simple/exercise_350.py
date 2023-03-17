"""
给你两个整数数组 nums1 和 nums2 ，请你以数组形式返回两数组的交集。返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/intersection-of-two-arrays-ii
"""
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        con = dict()
        res = []
        for num in nums1:
            con.setdefault(num, 0)
            con[num] += 1

        for num in nums2:
            if num in con:
                if con[num] > 0:
                    con[num] -= 1
                    res.append(num)
                    continue
        return res


solution = Solution()
print(solution.intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))
