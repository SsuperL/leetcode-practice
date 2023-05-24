"""
二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor_2(self, root, p, q):
        """递归+回溯"""

        def traverse(root):
            if not root or root == p or root == q:
                return root
            pre_left = traverse(root.left)
            pre_right = traverse(root.right)
            if pre_left and pre_right:
                return root
            if pre_left:
                return pre_left

            return pre_right

        res = traverse(root)
        return res
