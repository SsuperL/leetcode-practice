"""
给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。

树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。
"""
from collections import deque
from typing import List

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        res = []
        q = deque()
        if not root:
            return res
        q.append(root)
        while q:
            tmp = []
            for k in range(len(q)):
                node = q.popleft()
                if isinstance(node, list):
                    for i in node:
                        tmp.append(i.val)
                        if i.children:
                            q.append(i.children)
                else:
                    tmp.append(node.val)
                    if node.children:
                        q.append(node.children)
            res.append(tmp)

        return res
