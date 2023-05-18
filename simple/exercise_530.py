"""
给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。

差值是一个正数，其数值等于两值之差的绝对值。
"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        迭代
        :param root:
        :return:
        """
        # 中序遍历
        # 正无穷
        res = float("INF")
        if not root:
            return int(res)
        stack = []
        cur = root
        pre = None
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                # 记录前一个节点的值
                if pre:
                    res = min(res, abs(cur.val - pre.val))
                pre = cur
                cur = cur.right

        return res

    def getMinimumDifference_2(self, root: Optional[TreeNode]) -> int:
        """
        递归
        :param root:
        :return:
        """
        res = []
        r = float("inf")

        def buildaList(root):
            # 把二叉搜索树转换成有序数组
            # 中序遍历
            if not root:
                return None
            if root.left:
                buildaList(root.left)  # 左
            res.append(root.val)  # 中
            if root.right:
                buildaList(root.right)  # 右
            return res

        buildaList(root)
        for i in range(len(res) - 1):
            # 统计有序数组的最小差值
            r = min(abs(res[i] - res[i + 1]), r)

        return r
