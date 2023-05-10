"""
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """迭代法"""
        if not root:
            return False
        stack = [root]
        value_stack = [root.val]
        while stack:
            # 深度优先，前序遍历
            node = stack.pop()
            value = value_stack.pop()
            if not node.left and not node.right and value == targetSum:
                return True
            if node.right:
                stack.append(node.right)
                value_stack.append(value + node.right.val)
            if node.left:
                stack.append(node.left)
                value_stack.append(value + node.left.val)

        return False

    def hasPathSum_2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        递归法
        使用递减法+回溯
        初始化 count 为 目标值，遇到一个节点，减去节点值，到达叶子节点且count为0，则找到正确路径
        如果未找到正确路径，需要回溯，加回减的节点值
        """
        count = targetSum
        if not root:
            return False

        def traverse(node, count):
            # 找到正确路径
            if not node.left and not node.right and count == 0:
                return True
            # 遇到叶子节点，但计数不为0
            if not node.left and not node.right:
                return False

            # 空节点不进入递归
            if node.left:
                count -= node.left.val
                if traverse(node.left, count):
                    return True
                # 回溯
                count += node.left.val
            if node.right:
                count -= node.right.val
                if traverse(node.right, count):
                    return True
                count += node.right.val
            return False

        return traverse(root, count - root.val)
