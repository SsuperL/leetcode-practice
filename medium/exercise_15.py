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
        res = []
        if len(nums) < 3:
            return res
        nums.sort()
        for i in range(len(nums)-2):
            if i == 0 or nums[i] > nums[i-1]:
                left = i+1
                right = len(nums)-1
                while left < right:
                    ident = nums[left] + nums[right] + nums[i]
                    if ident == 0:
                        res.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        # 去除重复结果
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif ident < 0:
                        left += 1
                    else:
                        right -= 1
        return res


solution = Solution()
print(solution.threeSum([-2, 0, 3, -1, 4, 0, 3, 4, 1, 1, 1, -3, -5, 4, 0]))
