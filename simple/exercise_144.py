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

    def preorderTraversal_3(self, root: Optional[TreeNode]) -> List[int]:
        """前序遍历：统一迭代法，前中后序遍历使用统一的迭代方法，使用栈+标记法，
        将待处理的节点入栈，将要处理的节点后入栈 None ，只有当 None 出栈后才能将其后的节点加入结果列表"""
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                # 空节点不入栈,先进后出
                if node.right:
                    # 右
                    stack.append(node.right)

                # 左
                if node.left:
                    stack.append(node.left)
                stack.append(node)
                # 在未处理的节点后做标记
                stack.append(None)
            else:
                node = stack.pop()
                res.append(node.val)

        return res
