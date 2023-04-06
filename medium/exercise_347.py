"""
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
"""
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tmp = dict()
        for i in nums:
            tmp.setdefault(i, 0)
            tmp[i]+=1

        pri_que=[]
        # 使用小顶堆实现，如果元素个数大于k，将堆顶元素弹出，保证堆只有k个元素
        for key,value in tmp.items():
            heapq.heappush(pri_que,(value,key))
            if len(pri_que)>k:
                heapq.heappop(pri_que)

        res =[0]*k
        # 将小顶堆堆元素倒叙弹出
        for i in range(k-1,-1,-1):
            res[i]=heapq.heappop(pri_que)[1]
        return res