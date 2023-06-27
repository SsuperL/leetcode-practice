"""
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtracking(nums, res, cur, start_index):
            res.append(cur[:])
            
            for i in range(start_index, len(nums)):
                # 去重，或者使用集合去重
                if i>start_index and nums[i]==nums[i-1]:
                    continue
                cur.append(nums[i])
                backtracking(nums, res, cur, i+1)
                cur.pop()
        
        res,cur = [],[]
        # 需要对集合做排序操作，后续去重
        nums = sorted(nums)
        backtracking(nums, res, cur,0)
        return res