"""
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/validate-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        递归
        采用中序遍历：二叉搜索树中序遍历结果是递增的！
        :param root:
        :return:
        """
        pre = None

        def traverse(node):
            nonlocal pre
            if not node:
                # 二叉搜索树节点可以为空
                return True
            is_valid_left = traverse(node.left)
            # 记录前一个节点的值，用于后续比较
            if pre and pre.val >= node.val:
                return False
            pre = node

            is_valid_right = traverse(node.right)
            return is_valid_left and is_valid_right

        return traverse(root)

    def isValidBST_2(self, root: Optional[TreeNode]) -> bool:
        """
        迭代: 中序遍历
        :param root:
        :return:
        """
        if not root:
            return False
        stack = []
        # 用于记录前一个节点的值，做比较
        pre = None
        cur = root
        while stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                # 二叉搜索树是递增的，前一个节点的值不应该大于等于当前节点值
                if pre and pre.val >= cur.val:
                    return False
                pre = cur
                cur = cur.right

        return True


# [5,1,4,null,null,6]
#         5
#       4   6
#          3  7
