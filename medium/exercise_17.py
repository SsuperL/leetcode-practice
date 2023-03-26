"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={
            '2':["a","b","c"],
            '3':["d","e","f"],
            '4':["g","h","i"],
            '5':["j","k","l"],
            '6':["m","n","o"],
            '7':["p","q","s","r"],
            '8':["t","u","v"],
            '9':["w","x","y","z"]
        }
        if len(digits)==0:
            return []

        ans=['']
        for i in digits:
            ans=[pre+suf for pre in ans for suf in d[i]]
        return ans
    
    def letterCombinations_2(self, digits):
        map = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        res = []
        s =''
        def backtracking(res,s,index):
            if index == len(digits): # 结束条件
                res.append(s)
                return

            digit=int(digits[index])

            letters = map[digit]
            for i in letters:
                s+=i
                backtracking(res,s,index+1) # 回溯下一个字符
                s=s[:-1] # 删除最后一个添加的字符
            
            return
        
        if len(digits)==0:
            return res
        
        backtracking(res,'',0)
        return res
        
         
            


solution=Solution()
print(solution.letterCombinations("234"))
