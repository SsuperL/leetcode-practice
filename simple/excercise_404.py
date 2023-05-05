"""
给定二叉树的根节点 root ，返回所有左叶子之和
"""
# Definition for a binary tree node.
# class TreeNode:
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                # 左叶子节点 : 节点有左孩子且左孩子无左孩子或右孩子
                if node.left and not node.left.right and not node.left.left:
                    res += node.left.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res

    def sumOfLeftLeaves_2(self, root):
        """递归"""
        self.res = 0

        def traverse(node):
            if not node:
                return
            if node and not node.left and not node.right:
                self.res += node.val

            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return self.res
