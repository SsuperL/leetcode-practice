"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """方法一：递归"""
        # 分别计算左右子树的高度，再比较差值
        if not root:
            return True

        def countDepth(node, depth):
            if not node:
                return True, depth
            depth += 1
            is_balanced_left, left_depth = countDepth(node.left, depth)
            is_balanced_right, right_depth = countDepth(node.right, depth)
            if not is_balanced_right or not is_balanced_left:
                return False
            if abs(left_depth - right_depth) > 1:
                return False, 0
            return True, max(left_depth, right_depth)

        left = root.left
        right = root.right
        is_balanced_left, left_depth = countDepth(left, 1)
        is_balanced_right, right_depth = countDepth(right, 1)
        if not is_balanced_right or not is_balanced_left:
            return False

        return abs(left_depth - right_depth) <= 1

    def isBalanced_2(self, root):
        """方法二，迭代法"""
        if not root:
            return True
        stack = [root]
        height_map = {}
        while stack:
            node = stack.pop()
            if node:
                stack.append(node)
                stack.append(None)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            else:
                real_node = stack.pop()
                left, right = (
                    height_map.get(real_node.left, 0),
                    height_map.get(real_node.right, 0),
                )
                if abs(left - right) > 1:
                    return False
                height_map[real_node] = 1 + max(left, right)
        return True
        #
