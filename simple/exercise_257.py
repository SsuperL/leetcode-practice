"""
给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。

叶子节点 是指没有子节点的节点。
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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """迭代法"""
        res = []
        if not root:
            return res
        # 使用两个栈，一个记录结果，一个记录节点
        stack = [root]
        path_stack = [str(root.val)]
        while stack:
            # 前序遍历，深度优先
            node = stack.pop()
            path = path_stack.pop()
            if not node.left or node.right:
                # 是叶子节点，将路径添加至结果集
                res.append(path)
            if node.right:
                stack.append(node.right)
                path_stack.append(f"{path}->{node.right.val}")
            if node.left:
                stack.append(node.left)
                path_stack.append(f"{path}->{node.left.val}")

        return res

    def binaryTreePaths_2(self, root):
        """递归+回溯"""

        def traverse(node, path, res):
            path += str(node.val)
            if not node.left and not node.right:
                res.append(path)

            # "->" 隐藏回溯
            if node.left:
                traverse(node.left, path + "->", res)
            if node.right:
                traverse(node.right, path + "->", res)

            if not root:
                return res

        res = []
        path = ""
        traverse(root, "", res)

        return res
