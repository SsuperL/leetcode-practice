"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/remove-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow, fast = 0, 0  # 使用快慢指针
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[
                    fast
                ]  # 快指针对应元素不等于val时，将慢指针对应元素与其替换(不需要考虑超出新长度后的元素），实现"删除"
                slow += 1
            fast += 1

        return slow


sol = Solution()
print(sol.removeElement([3, 2, 2, 3, 4], val=3))
print(sol.removeElement([0, 1, 2, 2, 3, 0, 4, 2], val=2))
