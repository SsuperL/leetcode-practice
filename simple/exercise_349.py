"""
给定两个数组 nums1 和 nums2 ，返回 它们的交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。
"""
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        con = set()
        res = set()
        for num in nums1:
            con.add(num)

        for num in nums2:
            if num in con:
                res.add(num)

        return list(res)


solution = Solution()
print(solution.intersection(nums1=[1, 2, 2, 1], nums2=[2, 2]))
