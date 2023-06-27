"""
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

回文串 是正着读和反着读都一样的字符串。
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path,result = [],[]
        def is_huiwen(s,slow,fast)->bool:
            """判断是否回文字符串"""
            while slow<fast:
                if s[slow]!=s[fast]:
                    return False
                slow+=1
                fast-=1
            return True
        
        def backtracking(s,path,result,start_index):
            # 遍历至末尾
            if start_index==len(s):
                result.append(path[:])
                return
            
            # for循环横向遍历字符串
            for i in range(start_index,len(s)):
                # 剪枝，先判断是否为回文字符串
                if is_huiwen(s,start_index,i):
                    # 递归纵向遍历切割条件
                    path.append(s[start_index:i+1])
                    backtracking(s,path,result,i+1)
                    path.pop()

        backtracking(s,path,result,0)
        return result
