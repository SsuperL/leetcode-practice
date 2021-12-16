"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
字符串中包含数字、字母及空格
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        m=0
        start=0
        dic={}
        for i in range(len(s)):
            if s[i] in dic and dic[s[i]]>=start:
                start=dic[s[i]]+1
            m=i-start+1
            dic[s[i]]=i
            max_len=max(max_len,m)
            
        return max_len

solution=Solution()
res=solution.lengthOfLongestSubstring("1")
res2=solution.lengthOfLongestSubstring("pwwkepw")
print(res)
print(res2)