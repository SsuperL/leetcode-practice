"""
找树左下角的值
给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。

假设二叉树中至少有一个节点。
"""
# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        """迭代法"""
        res = None
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        q = deque([root])
        # 树的最大深度？
        while q:
            for i in range(len(q)):
                node = q.popleft()
                # 依次迭代，如果节点均没有孩子，返回第一个节点的值，否则取第一个有孩子的节点的值
                if not node.left and not node.right and i == 0:
                    res = node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res

    def findBottomLeftValue_2(self, root: Optional[TreeNode]) -> int:
        """递归法"""
        max_depth = -float("INF")
        leftmost_val = 0

        def __traverse(root, cur_depth):
            nonlocal max_depth, leftmost_val
            if not root.left and not root.right:
                if cur_depth > max_depth:
                    max_depth = cur_depth
                    leftmost_val = root.val
            if root.left:
                cur_depth += 1
                __traverse(root.left, cur_depth)
                cur_depth -= 1
            if root.right:
                cur_depth += 1
                __traverse(root.right, cur_depth)
                cur_depth -= 1

        __traverse(root, 0)
        return leftmost_val
