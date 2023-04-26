# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                res += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
