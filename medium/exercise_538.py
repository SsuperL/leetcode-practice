"""
给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。

提醒一下，二叉搜索树满足下列约束条件：

节点的左子树仅包含键 小于 节点键的节点。
节点的右子树仅包含键 大于 节点键的节点。
左右子树也必须是二叉搜索树。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/convert-bst-to-greater-tree
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
    def __init__(self):
        self.count = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        递归，反中序遍历
        使用pre记录前一个节点的值
        :param root:
        :return:
        """
        if not root:
            return

        # 右节点
        root.right = self.convertBST(root.right)
        # 中
        self.count += root.val
        root.val += self.count
        # 左节点
        root.left = self.convertBST(root.left)

        return self.convertBST(root)

    def convertBST_2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """迭代"""
        if not root:
            return None
        stack = []
        cur = root
        pre = 0
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                cur.val += pre
                pre = cur.val
                cur = cur.left

        return root
