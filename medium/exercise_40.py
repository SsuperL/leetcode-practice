"""
给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用 一次 。

注意：解集不能包含重复的组合。 

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res,path=[],[]

        def backtracking(startIndex: int, res,path,current):
            
            if current == target:
                res.append(path[:])
                return
            
            for i in range(startIndex,len(candidates)):
                if current+candidates[i]>target:
                    break
                if i >startIndex and candidates[i]==candidates[i-1]:
                    continue
                current+=candidates[i]
                path.append(candidates[i])
                backtracking(i+1, res,path,current)
                current-=candidates[i]
                path.pop()
        
        candidates.sort()
        backtracking(0, res,path,0)
        return res
    
    # 使用used数组，排除掉回溯过程中已经使用过的数字
    # def backtracking(self, candidates, target, total, startIndex, used, path, result):
    #     if total == target:
    #         result.append(path[:])
    #         return

    #     for i in range(startIndex, len(candidates)):
    #         # 对于相同的数字，只选择第一个未被使用的数字，跳过其他相同数字
    #         if i > startIndex and candidates[i] == candidates[i - 1] and not used[i - 1]:
    #             continue

    #         if total + candidates[i] > target:
    #             break

    #         total += candidates[i]
    #         path.append(candidates[i])
    #         used[i] = True
    #         self.backtracking(candidates, target, total, i + 1, used, path, result)
    #         used[i] = False
    #         total -= candidates[i]
    #         path.pop()

    # def combinationSum2(self, candidates, target):
    #     used = [False] * len(candidates)
    #     result = []
    #     candidates.sort()
    #     self.backtracking(candidates, target, 0, 0, used, [], result)
    #     return result
