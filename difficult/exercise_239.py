"""
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/sliding-window-maximum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import queue
from collections import deque
from typing import List


class MyQueue:
    """
    使用单调队列实现
    该题中是单调递增队列，队列入口元素为最大元素
    队列中只维护可能是最大值的元素
    """

    def __init__(self):
        self.queue = deque()

    def pop(self, x):
        """弹出元素"""
        if x == self.queue[0]:
            # 每次弹出判断元素是否大于等于队头元素，大于等于则弹出
            self.queue.popleft()  # 如果使用list的话，pop的时间复杂度是O(n)

    def push(self, x):
        """如果入队元素大于队头元素，则把小于入队元素的都出队，否则不做改变"""
        while self.queue and x > self.queue[-1]:
            # 如果入队元素大于队列入口（队尾）元素，则把小于等于入队元素的都弹出
            self.queue.pop()  # 弹出队尾元素
        self.queue.append(x)

    def top(self):
        return self.queue[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = MyQueue()
        for i in range(k):
            queue.push(nums[i])
        res = [queue.top()]
        right = k
        while right < len(nums):
            # 弹出滑动窗口左边界元素
            print(right - k)
            print("---", queue.top())
            queue.pop(nums[right - k])
            # 加入滑动窗口右边界元素
            queue.push(nums[right])
            res.append(queue.top())
            right += 1
        return res


solution = Solution()
# print(solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
# print(solution.maxSlidingWindow([1,-1],1))
# print(solution.maxSlidingWindow([1],1))
# print(solution.maxSlidingWindow([7,2,4],2))
print(solution.maxSlidingWindow([9, 10, 9, -7, -4, -8, 2, -6], 5))
