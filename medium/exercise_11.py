"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
[1,8,6,2,5,4,8,3,7]
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 使用双头指针，向中间移动
        start, end = 0, len(height)-1
        max_area = 0
        for i in height:
            area = min(height[start], height[end])*(end-start)
            max_area = max(area, max_area)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max_area


solution = Solution()
print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
