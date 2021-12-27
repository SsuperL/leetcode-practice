"""
给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。

返回这三个数的和。

假定每组输入只存在恰好一个解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        # 存储最小差值
        min_diff = 0
        for i in range(len(nums)-2):
            if i == 0 or nums[i] > nums[i-1]:
                left = i+1
                right = len(nums)-1
                while left < right:
                    tmp = nums[i] + nums[left] + nums[right]
                    if min_diff == 0:
                        min_diff = abs(tmp-target)
                        res = tmp

                    # 差值与三数之和比较
                    elif abs(tmp-target) < min_diff:
                        min_diff = abs(tmp-target)
                        res = tmp
                    if tmp == target:
                        return target
                    if tmp < target:
                        left += 1
                    if tmp > target:
                        right -= 1
        return res


solution = Solution()
print(solution.threeSumClosest([1, 1, 1, 0], 3))
