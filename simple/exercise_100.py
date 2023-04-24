"""
给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的
"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        stack_p = [p]
        stack_q = [q]
        while stack_q:
            node_p = stack_p.pop()
            node_q = stack_q.pop()
            if not node_p and not node_q:
                continue
            if (not node_p or not node_q) or node_p.val != node_q.val:
                return False
            stack_p.append(node_p.left)
            stack_p.append(node_p.right)
            stack_q.append(node_q.left)
            stack_q.append(node_q.right)
        if stack_p != stack_q:
            return False
        return True
