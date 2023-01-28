"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/search-insert-position
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # if not nums:
        #     return 0
        # if len(nums) == 1:
        #     if nums[0] == target:
        #         return 0
        #     if nums[0]<target:
        #         return 1
        #     else:
        #         return 0
        start,end = 0,len(nums)-1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return end+1

solution = Solution()
print(solution.searchInsert(nums = [1,3,5,6], target = 5))
print(solution.searchInsert(nums = [1,3,5,6], target = 2))
print(solution.searchInsert(nums = [1,3,5,6], target = 7))
print(solution.searchInsert(nums = [1,3,5,6], target = 0))