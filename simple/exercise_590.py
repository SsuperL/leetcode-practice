"""
给定一个 n叉树的根节点root，返回 其节点值的 后序遍历 。

n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/n-ary-tree-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node) -> List[int]:
        res = []

        def traverse(node):
            if not node:
                return
            for i in sorted(node.children, reverse=True):
                traverse(i)
            res.append(node.val)

        traverse(root)
        return res
