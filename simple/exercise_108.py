"""
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。

高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree
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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """递归"""
        if not nums:
            return
        # 取中间节点作为树的根节点
        root_index = len(nums) // 2
        root_val = nums[root_index]
        left_nums = nums[0:root_index]
        right_nums = nums[root_index + 1 :]
        root = TreeNode(root_val)
        root.left = self.sortedArrayToBST(left_nums)
        root.right = self.sortedArrayToBST(right_nums)

        return root

    def sortedArrayToBST_2(self, nums: List[int]) -> Optional[TreeNode]:
        """迭代"""
        if len(nums) == 0:
            return None
        root = TreeNode()  # 初始化
        nodeSt = [root]  # 遍历所有节点
        leftSt = [0]  # 左区间初始下标
        rightSt = [len(nums)]  # 右区间初始下标

        while nodeSt:
            node = nodeSt.pop()  # 处理根节点
            left = leftSt.pop()
            right = rightSt.pop()
            mid = left + (right - left) // 2
            node.val = nums[mid]

            if left < mid:  # 处理左区间
                node.left = TreeNode()
                nodeSt.append(node.left)
                leftSt.append(left)
                rightSt.append(mid)

            if right > mid + 1:  # 处理右区间
                node.right = TreeNode()
                nodeSt.append(node.right)
                leftSt.append(mid + 1)
                rightSt.append(right)

        return root
