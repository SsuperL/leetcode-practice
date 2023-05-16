"""
给你两棵二叉树： root1 和 root2 。

想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；否则，不为 null 的节点将直接作为新二叉树的节点。

返回合并后的二叉树。

注意: 合并过程必须从两个树的根节点开始。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/merge-two-binary-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        """递归"""
        # 只要其中一个节点为空就返回另一个节点
        if not root1:
            return root2
        if not root2:
            return root1
        # 目的是合并树，不是创建树，节约空间和时间
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)

        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1

    def mergeTrees_2(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        """迭代，将两棵树的节点加入同一队列处理"""
        if not root1:
            return root2
        if not root2:
            return root1

        q = deque([root1, root2])
        while q:
            node1, node2 = q.popleft(), q.popleft()
            # 两个树的左右子节点都不为空时才加入队列
            if node1.left and node2.left:
                q.append(node1.left)
                q.append(node2.left)
            if node1.right and node2.right:
                q.append(node1.right)
                q.append(node2.right)

            # 更新当前节点值，并更新当前节点的左右孩子
            node1.val += node2.val
            if not node1.left and node2.left:
                node1.left = node2.left
            if not node1.right and node2.right:
                node1.right = node2.right

        return root1
