"""
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
"""
# Definition for a binary tree node.
from collections import deque
from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """层序遍历"""
        res = []
        q = deque()
        if not root:
            return res
        q.append(root)
        while q:
            tmp = None
            for i in range(len(q)):
                node = q.popleft()
                # 从左往右层级遍历，如果右边节点不为空，则替换tmp的值，最后保存到res中的是最右边节点的值
                if node:
                    tmp = node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            res.append(tmp)

        return res


solution = Solution()
print(
    solution.rightSideView(
        TreeNode(
            1,
            left=TreeNode(2, left=TreeNode(4, left=TreeNode(8)), right=TreeNode(5)),
            right=TreeNode(3, left=TreeNode(6), right=TreeNode(7)),
        )
    )
)
print(
    solution.rightSideView(
        TreeNode(1, left=TreeNode(2, left=TreeNode(4)), right=TreeNode(3))
    )
)
print(
    solution.rightSideView(
        TreeNode(
            1, left=TreeNode(2, right=TreeNode(5)), right=TreeNode(3, right=TreeNode(4))
        )
    )
)
#    1
#  2  3
# 4 5 6 7
# 8
