"""
给定一个非空的字符串 s ，检查是否可以通过由它的一个子串重复多次构成
"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # 使用KMP算法
        def getPrefix(s):
            # 构造前缀表
            j,i=0,1
            pref=[0]*len(s)
            while i < len(s):
                while j>0 and s[i]!=s[j]:
                    j=pref[j-1]
                if s[i]==s[j]:
                    j+=1
                pref[i]=j
                i+=1
            return pref
        
        pref = getPrefix(s)
        # 字符串长度减去最长公共前后缀（pref[-1]）长度
        # 如果存在重复字符串，则最长相同前缀和最长相同后缀不匹配的部分就是重复字符串（即字符串减去最长公共前后缀的部分）
        # 数组长度减去最长相同前后缀的长度相当于是第一个周期的长度，也就是一个周期的长度，如果这个周期可以被整除，就说明整个数组就是这个周期的循环。
        tmp=(len(s)-len(pref[-1]))
        if pref[-1]!=0 and len(s)%tmp==0:
            return True        
        return False
    


       
        
solution = Solution()
print(solution.repeatedSubstringPattern("abac"))
print(solution.repeatedSubstringPattern("abcabcabcabc"))