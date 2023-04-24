"""
给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true ；否则，返回 false 。

二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/subtree-of-another-tree
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return False

        def isSameTree(p, q):
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

        stack = [root]
        # 逐一比较子树是否目标子树
        while stack:
            node = stack.pop()
            if isSameTree(node, subRoot):
                return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return False
