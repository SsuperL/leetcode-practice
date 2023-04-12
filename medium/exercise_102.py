"""
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
"""
# Definition for a binary tree node.
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """层序遍历（先进先出）适合用队列，深度优先遍历适合用栈"""
        res = []
        if not root:
            return res

        que = deque()
        que.append(root)
        while que:
            tmp = []
            for i in range(len(que)):
                node = que.popleft()
                tmp.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(tmp)
        return res

    def levelOrder_2(self, root: Optional[TreeNode]) -> List[List[int]]:
        """层序遍历：递归"""
        res = []
        if not root:
            return res

        def traverse(node, depth):
            """
            :param node: 节点
            :param depth: 所处层级
            :return:
            """
            if not node:
                return
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            if node.left:
                traverse(node.left, depth + 1)
            if node.right:
                traverse(node.right, depth + 1)

        traverse(root, 0)
        return res
