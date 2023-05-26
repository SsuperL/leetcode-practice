"""
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

首先找到需要删除的节点；
如果找到了，删除它。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/delete-node-in-a-bst
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
    def deleteNode_2(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """迭代"""
        # 找到节点后分两步，1. 把节点的左子树和右子树连起来，2. 把右子树跟父节点连起来
        # root is None
        if not root:
            return root
        p = root
        last = None
        while p:
            if p.val == key:
                # 1. connect left to right
                # right is not None -> left is None | left is not None
                if p.right:
                    if p.left:
                        node = p.right
                        while node.left:
                            node = node.left
                        node.left = p.left
                    right = p.right
                else:
                    # right is None -> right=left
                    right = p.left
                # 2. connect right to last
                if last == None:
                    root = right
                elif last.val > key:
                    last.left = right
                else:
                    last.right = right
                # 3. return
                break
            else:
                # Update last and continue
                last = p
                if p.val > key:
                    p = p.left
                else:
                    p = p.right
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """递归"""
        # 1) 没找到key 或者节点为叶子节点
        if not root:
            return None
        # 2）找到key
        if root.val == key:
            # 2) 只有左节点
            if not root.right:
                return root.left
            # 3) 只有右节点
            elif not root.left:
                return root.right
            else:
                # 右子树的根节点顶替当前节点，左子树放到右子树最左边孩子的左节点上（二叉搜索树有序性）
                node = root.right
                while node.left:
                    node = node.left
                node.left = root.left
                root = root.right
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
