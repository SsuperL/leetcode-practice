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

    def postorderTraversal_2(self, root: Optional[TreeNode]) -> List[int]:
        """后序遍历：迭代法"""
        # 前序遍历顺序是：中->左->右, 调整遍历顺序：中->右->左，再反转数组即得到后序遍历（左->右->中）结果
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                return res
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return res[::-1]

    def postorderTraversal_3(self, root: Optional[TreeNode]) -> List[int]:
        """后序遍历：统一迭代法，使用栈+标记法"""
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                # 空节点不入栈，先进后出
                stack.append(node)
                # 在未处理的节点后做标记
                stack.append(None)
                if node.right:
                    # 右
                    stack.append(node.right)

                # 左
                if node.left:
                    stack.append(node.left)
            else:
                node = stack.pop()
                res.append(node.val)

        return res
