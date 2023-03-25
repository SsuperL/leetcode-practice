"""
给你两个字符串haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果needle 不是 haystack 的一部分，则返回  -1 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 方法一：使用滑动窗口实现
        # left, right = 0, len(needle) - 1
        # while right < len(haystack):
        #     if haystack[left : right + 1] == needle:
        #         return left
        #     left += 1
        #     right += 1
        # return -1

        # 方法二：KMP
        def getPrefix(needle):
            # 构造模式串的前缀表
            # j 指向前缀字符串的末尾位置，i指向后缀字符串的末尾位置
            j,i=0,1
            pref=[0]*len(needle)
            # 初始化pref[j] = 0
            # pref[i]表示i（含i）之前的前缀字符和后缀字符串相等的长度，即j
            pref[j]=0
            while i < len(needle)-1:
                while j >0 and needle[j]!=needle[i]:
                    # 前后缀长度不相等时，需要回退，即回退至 j-1 位置
                    j = pref[j-1]
                if needle[i]==needle[j]:
                    j+=1
                    # i（含i）之前的前缀字符和后缀字符串相等的长度，即j
                pref[i] = j
                i +=1
            return pref
                
        pref = getPrefix(needle)
        i, j = 0,0
        for i in range(len(haystack)):
            while j >0 and haystack[i]!=needle[j]:
                # 不匹配时回退至前一个匹配的地方
                j=pref[j-1]
            if haystack[i]==needle[j]:
                j += 1
            if j == len(needle):
                # 长度相等，即完全匹配时，返回第一个匹配的字符索引
                return i - len(needle)+1
            
        return -1
            


solution = Solution()
print(solution.strStr(haystack="sadbutsad", needle="sad"))
print(solution.strStr(haystack="leetcode", needle="leeto"))
