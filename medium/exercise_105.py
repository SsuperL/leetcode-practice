"""
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        递归
        前序数组中的第一个元素即为二叉树的根节点，根据该元素切割中序数组，得到左序数组和右中序数组
        中序数组和后续数据原始大小相等，可以根据切割后的中序数组切割后序数组，再得到前序数组中的第一个元素
        （再继续之前的步骤）
        :param preorder:
        :param inorder:
        :return:
        """
        if not preorder:
            return

        pre = preorder[0]
        root_index = inorder.index(pre)
        root = TreeNode(pre)

        # 切割中序数组
        inorder_left = inorder[:root_index]
        inorder_right = inorder[root_index + 1 :]

        # 切割前序数组
        pre_left = preorder[1 : len(inorder_left) + 1]
        pre_right = preorder[len(inorder_left) + 1 :]

        root.left = self.buildTree(pre_left, inorder_left)
        root.right = self.buildTree(pre_right, inorder_right)

        return root


# preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
