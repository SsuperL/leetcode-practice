"""
整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

 

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/search-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # binary search
        def find_max(nums):
            # 查找旋转所在位置，即数组最大值索引，如果未旋转则返回-1
            start,end = 0,len(nums)-1
            while start <= end:
                mid = (start+end)//2
                mid_number = nums[mid]
                if mid>0 and mid_number<nums[mid-1]:
                    return mid -1
                elif nums[mid]< nums[-1]:
                    end = mid -1
                else:
                    start = mid +1
            return -1
        
        if nums[0]<nums[-1]:
            max_num_index = -1
        else:
            max_num_index = find_max(nums)
        # 有旋转
        if max_num_index !=-1:
            if target > nums[max_num_index]:
                return -1
            if target==nums[max_num_index]:
                return max_num_index
            if target<=nums[-1]:
                # 确定target元素所在范围
                start = max_num_index + 1
                end = len(nums)-1
            else:
                start,end =0,max_num_index
        else:
            start,end =0, len(nums)-1
        
        while start <= end:
            mid = (start+end)//2
            if target==nums[mid]:
                return mid
            if target>nums[mid]:
                start=mid+1
            else:
                end=mid-1
        return -1
solution = Solution()
res=solution.search([1,3,5],5)
print(res)