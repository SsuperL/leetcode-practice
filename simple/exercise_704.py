"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/binary-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if len(nums)==1:
            if nums[0] == target:
                return 0
            else:
                return -1
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid]>target:
                end = mid -1
            else:
                start=mid+1
        return -1


solution = Solution()
print(solution.search([-1,0,3,5,9,12], target = 9))
print(solution.search([2,5],5))
print(solution.search(nums = [-1,0,3,5,9,12], target = 2))
