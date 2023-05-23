"""
给你一个含重复值的二叉搜索树（BST）的根节点 root ，找出并返回 BST 中的所有 众数（即，出现频率最高的元素）。

如果树中有不止一个众数，可以按 任意顺序 返回。

假定 BST 满足如下定义：

结点左子树中所含节点的值 小于等于 当前节点的值
结点右子树中所含节点的值 大于等于 当前节点的值
左子树和右子树都是二叉搜索树

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-mode-in-binary-search-tree
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
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        """
        递归
        :param root:
        :return:
        """
        pass

    def findMode_2(self, root: Optional[TreeNode]) -> List[int]:
        """
        迭代
        :param root:
        :return:
        """
        res = []
        pre = None
        count, max_count = 0, 0
        stack = []
        if not root:
            return res
        cur = root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre and pre.val == cur.val:
                    count += 1
                elif not pre:
                    # 第一个节点
                    count = 1
                else:
                    # 重置count
                    count = 1
                if count > max_count:
                    max_count = count
                    res.clear()
                    res.append(cur.val)
                elif count == max_count:
                    res.append(cur.val)

                pre = cur
                cur = cur.right

        return res
