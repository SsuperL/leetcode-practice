"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """排序后使用双指针"""
        res = []
        if len(nums) < 3:
            return res
        nums.sort()
        # 排序后的第一个元素大于0，则已经无法凑成=0的三元组
        if nums[0] > 0:
            return res
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            # 去除重复结果
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 双指针遍历
            while left < right:
                ident = nums[left] + nums[right] + nums[i]
                if ident == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif ident < 0:
                    left += 1
                else:
                    right -= 1
        return res


solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
print(solution.threeSum([-2, 0, 3, -1, 4, 0, 3, 4, 1, 1, 1, -3, -5, 4, 0]))
print(solution.threeSum([0, 0, 0, 0]))
print(solution.threeSum([3, 0, -2, -1, 1, 2]))
