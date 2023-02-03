"""
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

 

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/minimum-size-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """使用滑动窗口实现"""
        init = float("inf")
        sum = 0
        i = 0
        for j in range(len(nums)):
            sum += nums[j]
            while sum >= target:
                init = min(init, j - i + 1)
                sum -= nums[i]
                i += 1

        return 0 if init == float("inf") else init


solution = Solution()
print(solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
