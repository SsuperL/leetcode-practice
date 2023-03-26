"""
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        start_index = 1
        # 横向遍历，纵向递归
        path=[]
        def back_racking(n,k,start_index):

            # 存放结果
            if len(path)==k:
                res.append(path[:])
                return

            # k-len(path) 为还需要的组合元素个数
            # n-k-len(path) 为至多从n中开始遍历的下标
            for i in range(start_index, n-(k-len(path))+2):
                path.append(i)
                back_racking(n,k,i+1)
                path.pop()
            
        back_racking(n,k,start_index)
        return res