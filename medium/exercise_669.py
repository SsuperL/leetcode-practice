"""
给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。通过修剪二叉搜索树，使得所有节点的值在[low, high]中。修剪树 不应该 改变保留在树中的元素的相对结构 (即，如果没有被移除，原有的父代子代关系都应当保留)。 可以证明，存在 唯一的答案 。

所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/trim-a-binary-search-tree
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
    def trimBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> Optional[TreeNode]:
        """
        递归
        :param root:
        :param low:
        :param high:
        :return:
        """
        if not root:
            return None

        # 大于右界限
        if root.val > high:
            # 左孩子替换当前节点，二叉搜索树的右节点必然大于当前节点
            return self.trimBST(root.left, low, high)
        # 小于左界限
        if root.val < low:
            # 右孩子替换当前节点，二叉搜索树的左节点必然小于当前节点
            return self.trimBST(root.right, low, high)

        # 替换当前节点的左右孩子
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root

    def trimBST_2(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> Optional[TreeNode]:
        """迭代"""
        if not root:
            return root
        # 处理头结点，让root移动到[L, R] 范围内，注意是左闭右开
        while root and (root.val < low or root.val > high):
            if root.val < low:  # 小于L往右走
                root = root.right
            else:  # 大于R往左走
                root = root.left
        # 此时root已经在[L, R] 范围内，处理左孩子元素小于L的情况
        cur = root
        while cur:
            while cur.left and cur.left.val < low:
                cur.left = cur.left.right
            cur = cur.left
        # 此时root已经在[L, R] 范围内，处理右孩子大于R的情况
        cur = root
        while cur:
            while cur.right and cur.right.val > high:
                cur.right = cur.right.left
            cur = cur.right
        return root
