"""
找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：

只使用数字1到9
每个数字 最多使用一次 
返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/combination-sum-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path = []
        res = []
        def backtracking(target, k, start, path, res, current):
            if current>target:
                return
            if len(path)==k:
                if current==target:
                    res.append(path[:])
                return
               
            
            for i in range(start,9-(k-len(path))+2):
                current+=i
                path.append(i)
                backtracking(target,k,i+1,path,res,current)
                current-=i
                path.pop()
        
        backtracking(n,k,1,path,res,0)
        return res

