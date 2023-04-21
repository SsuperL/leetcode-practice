"""
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        if not root:
            return
        q.append(root)
        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root

    def invertTree_2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        前序遍历
        :return:
        """
        stack = []
        if not root:
            return
        stack.append(root)
        while stack:
            node = stack.pop()
            if node.left or node.right:
                node.left, node.right = node.right, node.left
                stack.append(node.right)
                stack.append(node)
                stack.append(node.left)
        return root
