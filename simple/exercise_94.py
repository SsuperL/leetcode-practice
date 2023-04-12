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

    def inorderTraversal_2(self, root: Optional[TreeNode]) -> List[int]:
        """中序遍历：迭代法"""
        # 使用指针+栈
        stack = []
        res = []
        cur = root
        while cur or stack:
            if cur:
                # 当前节点不为空时持续将其和其左子节点入栈
                stack.append(cur)
                # 遍历左层子节点，直至最底层
                cur = cur.left
            else:
                # 出栈并保存结果
                cur = stack.pop()
                res.append(cur.val)
                # 将右子节点在下一个循环中入栈
                cur = cur.right
        return res

    def inorderTraversal_3(self, root: Optional[TreeNode]) -> List[int]:
        """中序遍历：统一迭代法，栈+标记法"""
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.right:
                    # 右
                    stack.append(node.right)
                # 空节点不入栈
                stack.append(node)
                # 在未处理的节点后做标记
                stack.append(None)
                # 左
                if node.left:
                    stack.append(node.left)
            else:
                node = stack.pop()
                res.append(node.val)

        return res
