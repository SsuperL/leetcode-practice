"""
给定二叉搜索树（BST）的根节点 root 和要插入树中的值 value ，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 输入数据 保证 ，新值和原始二叉搜索树中的任意节点值都不同。

注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回 任意有效的结果 。



来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/insert-into-a-binary-search-tree
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
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """递归"""
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)

        return root

    def insertIntoBST_2(self, root: Optional, val: int) -> Optional[TreeNode]:
        """
        迭代
        前序遍历
        :param root:
        :param val:
        :return:
        """
        if not root:
            return TreeNode(val)
        stack = [root]
        while stack:
            node = stack.pop()
            if val > node.val:
                if node.right:
                    stack.append(node.right)
                else:
                    node.right = TreeNode(val)
            if val < node.val:
                if node.left:
                    stack.append(node.left)
                else:
                    node.left = TreeNode(val)

        return root
