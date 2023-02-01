"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

 

示例 1：

输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]
示例 2：

输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/squares-of-a-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

# 原数组递增
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 数组按升序排序，只需比较两端最大值，并降序依次赋值给新数组
        left, right = 0, len(nums) - 1
        i = len(nums) - 1
        result = [i for i in range(len(nums))]
        while i >= 0:
            if nums[left] * nums[left] > nums[right] * nums[right]:
                result[i] = nums[left] * nums[left]
                left += 1
            else:
                result[i] = nums[right] * nums[right]
                right -= 1
            i -= 1

        return result


solution = Solution()

print(solution.sortedSquares([-4, -1, 0, 3, 10]))
