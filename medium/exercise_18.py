"""
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """使用双指针"""
        nums.sort()
        res = []
        if len(nums) < 4:
            return res
        n = len(nums)
        for i in range(len(nums) - 3):
            # 对i去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 四元组第二个元素的循环
            for j in range(i + 1, len(nums) - 2):
                # 对 j 去重
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # 循环内相向双指针
                left, right = j + 1, n - 1
                while left < right:
                    tmp = nums[left] + nums[right] + nums[i] + nums[j]
                    if tmp == target:
                        res.append([nums[left], nums[right], nums[i], nums[j]])
                        left += 1
                        right -= 1
                        # 去重
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif tmp > target:
                        right -= 1
                    else:
                        left += 1
        return res


soluton = Solution()
print(soluton.fourSum([1, 0, -1, 0, -2, 2], 0))
