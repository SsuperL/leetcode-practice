"""
路径总和II
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点。



来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/path-sum-ii
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """递归+回溯"""
        path_list = []
        path = []
        if not root:
            return []

        def traverse(node, count):
            if not node.left and not node.right and count == 0:
                # 需要使用切片方式
                path_list.append(path[:])
                return

            if node.right and not node.right:
                return
            if node.left:
                count -= node.left.val
                path.append(node.left.val)
                traverse(node.left, count)
                # 回溯
                count += node.left.val
                path.pop()

            if node.right:
                count -= node.right.val
                path.append(node.right.val)
                traverse(node.right, count)
                count += node.right.val
                path.pop()

            return

        path.append(root.val)
        traverse(root, targetSum - root.val)
        return path_list

    def pathSum_2(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """迭代"""
        res, paths = [], []
        if not root:
            return res

        count = targetSum - root.val
        stack = [root]
        # 使用一个额外栈存储当时的count和当时遍历的节点对应的path
        paths = [(count, [root.val])]
        while stack:
            node = stack.pop()
            count, path = paths.pop()
            print(count)
            print(path)
            if not node.left and not node.right and count == 0:
                res.append(path)

            if node.right:
                # 记录此刻的count和path
                paths.append((count - node.right.val, path + [node.right.val]))
                stack.append(node.right)

            if node.left:
                # 记录此刻的count和path
                paths.append((count - node.left.val, path + [node.left.val]))
                stack.append(node.left)

        return res


# 22
#     5
#  4      8
# 11    13 14
# 7 2      5 1
