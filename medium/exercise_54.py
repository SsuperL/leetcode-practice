"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up, down, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        res = []
        while len(res) < len(matrix) * len(matrix[0]):
            if up <= down:
                # 从左到右读取
                for i in range(left, right + 1):
                    res.append(matrix[up][i])
                up = up + 1
            if left <= right:
                # 从上到下读取
                for i in range(up, down + 1):
                    res.append(matrix[i][right])
                right = right - 1
            if up <= down:
                # 从右到左读取
                for i in range(right, left - 1, -1):
                    res.append(matrix[down][i])
                down = down - 1
            if left <= right:
                # 从下到上读取
                for i in range(down, up - 1, -1):
                    res.append(matrix[i][left])
                left = left + 1
        return res


solution = Solution()
# print(solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
# print(solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(solution.spiralOrder([[1]]))
print(solution.spiralOrder([[2, 5, 8], [4, 0, -1]]))
print(solution.spiralOrder([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]))
print(solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(
    solution.spiralOrder(
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    )
)
print(solution.spiralOrder([[2, 5], [8, 4], [0, -1]]))
