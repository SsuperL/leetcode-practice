"""
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """前序遍历节点顺序为：中左右"""
        # 递归法
        # 结束条件：当前遍历节点为空
        res = []

        def traverse(root):
            if not root:
                return
            # 中节点
            res.append(root.val)
            # 左节点
            traverse(root.left)
            # 右节点
            traverse(root.right)

        traverse(root)
        return res

    def preorderTraversal_2(self, root: Optional[TreeNode]) -> List[int]:
        """前序遍历：迭代法"""
        # 使用栈实现
        # 节点入栈顺序为： 中节点-> 右节点 -> 左节点
        res = []
        if not root:
            return []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                return res
            res.append(node.val)
            # 先让右节点先于左节点入栈，保证出栈顺序是中->左->右
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
