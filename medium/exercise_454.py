"""
给你四个整数数组 nums1、nums2、nums3 和 nums4 ，数组长度都是 n ，请你计算有多少个元组 (i, j, k, l) 能满足：

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/4sum-ii
"""
from typing import List


class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        tmp = dict()
        # 记录前两个数组的和，及对应的出现次数
        for a in nums1:
            for b in nums2:
                tmp.setdefault(a + b, 0)
                tmp[a + b] += 1

        count = 0
        for c in nums3:
            for d in nums4:
                # 0 - (c + d) 对应tmp中的key，即 a + b
                key = 0 - (c + d)
                if key in tmp:
                    count += tmp[key]

        return count
