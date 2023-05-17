"""
给定二叉搜索树（BST）的根节点 root 和一个整数值 val。

你需要在 BST 中找到节点值等于 val 的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 null 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/search-in-a-binary-search-tree
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
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """递归"""
        # 二叉搜索树是有序树，左子树小于根节点，右子树大于根节点
        if not root or root == val:
            return root

        if val > root.val:
            return self.searchBST(root.right, val)
        if val < root.val:
            return self.searchBST(root.left, val)

    def searchBST_2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """迭代"""
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == val:
                return node
            if node.right and val > node.val:
                stack.append(node.right)

            if node.left and val < node.val:
                stack.append(node.left)

        return

        # 或者
        # while root:
        #     if root.val == val:
        #         return root
        #     if root.val<val:
        #         root = root.right
        #     if root.val>val:
        #         root = root.left
        # return
