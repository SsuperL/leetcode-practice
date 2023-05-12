"""
给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。

 

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        递归：
        后续数组中的最后一个元素即为二叉树的根节点，根据该元素切割中序数组，得到左序数组和右中序数组
        中序数组和后续数据原始大小相等，可以根据切割后的中序数组切割后序数组，再得到后序数组中的最后一个元素
        （再继续之前的步骤）
        :param inorder:
        :param postorder:
        :return:
        """
        if not inorder:
            return
        # 后序数组最后一个节点即根节点
        root_node = postorder[-1]
        root = TreeNode(root_node)
        root_index = inorder.index(root_node)

        # 切割中序数组
        in_left = inorder[:root_index]
        in_right = inorder[root_index + 1 :]

        # 原始中序数组跟原始后续数组大小一定相等，可以根据切割后的中序数组来切割后续数组
        post_left = postorder[: len(in_left)]
        post_right = postorder[len(in_left) : len(postorder) - 1]

        root.left = self.buildTree(in_left, post_left)
        root.right = self.buildTree(in_right, post_right)

        return root


# inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
