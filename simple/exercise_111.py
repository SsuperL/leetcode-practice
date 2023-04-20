"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
"""
# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = deque()
        if not root:
            return res
        q.append(root)
        while q:
            res += 1
            for i in range(len(q)):
                node = q.popleft()
                if not node.left and not node.right:
                    return res
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
