"""
给定一个非空二叉树的根节点 root , 以数组的形式返回每一层节点的平均值。与实际答案相差 10-5 以内的答案可以被接受
"""
# Definition for a binary tree node.
from collections import deque
from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = deque()
        if not root:
            return res
        q.append(root)
        while q:
            sum_num = 0
            for i in range(len(q)):
                node = q.popleft()
                sum_num += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(sum_num / len(q))
        return res
