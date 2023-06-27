"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cur,res = [], []
        def backtraing(nums, start_index, res, cur):
            res.append(cur[:])
            # 不需要终止条件，for循环遍历结束会自动退出递归
            
            # 从start_index开始，避免重复遍历
            for i in range(start_index,len(nums)):
                cur.append(nums[i])
                # 纵向递归
                backtraing(nums, i+1, res, cur)
                cur.pop()
        
        backtraing(nums, 0, res, cur)

        return res              

