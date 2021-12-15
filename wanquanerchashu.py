# 给定一个二叉树，确定它是否是一个完全二叉树。
# 若设二叉树的深度为 h，除第 h 层外，其它各层 (1～h-1) 的结点数都达到最大个数，第 h 层所有的结点都连续集中在最左边，这就是完全二叉树。（注：第 h 层可能包含 1~ 2h 个节点。）
# 解题思路：使用队列遍历结点，遇到null则判断其后是否还有结点，若有则非完全二叉树（pop出结点后遇到null，set集合中不为空则为非完全二叉树）
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        que = []
        que.add(root)
        for i in range(100):
            node = que.pop(0)
            if node == None:
                if set(que) == {None}:
                    return True
                else:
                    return False
            que.append(node.left)
            que.append(node.right)
