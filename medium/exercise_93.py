"""
有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你 不能 重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。

 

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/restore-ip-addresses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res,path=[],''
        def backtracking(res,path,start_index,point_num,s):
            if point_num == 3:
                #小数点个数为3表示分割结束，判断最后一段字符是否合法
                if is_valid(s,start_index,len(s)-1):
                    path+=s[start_index:]
                    res.append(path[:])
                return
            
            for i in range(start_index,len(s)-1):
                if is_valid(s,start_index,i):
                    backtracking(res,path+s[start_index:i+1]+'.',i+1,point_num+1,s)
                else:
                    break

        def is_valid(s,start,end):
            if start>end:
                return False
            if s[start]=='0' and start!=end:
                return False
            num=int(s[start:end+1])
            return 0<=num<=255
        
        backtracking(res,path,0,0,s)
        return res

        
        