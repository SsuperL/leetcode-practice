"""
给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
"""
# Definition for a binary tree node.
from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """中序遍历节点顺序为：左中右节点"""
        res = []

        def traverse(root):
            if not root:
                return

            # 左节点
            traverse(root.left)
            # 中节点
            res.append(root.val)
            # 右节点
            traverse(root.right)

        traverse(root)
        return res
