"""
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

对于给定的输入，保证和为 target 的不同组合数少于 150 个。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path=[]
        # 同一个集合求组合元素时需要传 start_index; 多个互不影响的集合求组合元素时不需要start_index（如电话号码的字母组合）
        def backtraking(current:int,res:List,path:List,start_index:int,candidates):
            if current == target:
                res.append(path[:])
                return
            
            for i in range(start_index,len(candidates)):
                # 剪枝：总和大于target就跳出循环
                if current+candidates[i]>target:
                    break
                current+=candidates[i]
                path.append(candidates[i])
                # 不加1表示可以重复读取
                backtraking(current,res,path,i)
                current-=candidates[i]
                path.pop()
        
        # 对集合排序，碰到大于target的元素可以直接中止递归
        candidates.sort()
        
        backtraking(0,res,path,0,candidates)
        return res
            

            

            