"""
给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。
"""
from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """后序遍历顺序为：左右中节点"""
        res = []

        def traverse(root):
            if not root:
                return
            # 左节点
            traverse(root.left)
            # 右节点
            traverse(root.right)
            # 中节点
            res.append(root.val)

        traverse(root)
        return res
