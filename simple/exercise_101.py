"""
（轴）对称二叉树
"""
# Definition for a binary tree node.
import queue
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """方法一：使用栈，判断对应对里侧和外侧节点是否相等"""
        if not root:
            return False
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            left_node, right_node = stack.pop(), stack.pop()
            # 成对判断左右子节点是否对应相等
            # 无左节点和右节点
            if not left_node and not right_node:
                continue
            if not left_node or not right_node or left_node.val != right_node.val:
                return False
            # 左树的左子节点和右树的右子节点一对
            stack.append(left_node.left)
            stack.append(right_node.right)
            # 左树的右子节点和右树的左子节点一对
            stack.append(left_node.right)
            stack.append(right_node.left)

        return True

    def isSymmetric_2(self, root):
        """使用队列"""
        q = queue.Queue()
        if not root:
            return False
        q.put(root.left)
        q.put(root.right)
        while not q.empty():
            left, right = q.get(), q.get()
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            q.put(left.left)
            q.put(right.right)
            q.put(left.right)
            q.put(right.left)
        return True
