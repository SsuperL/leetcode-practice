"""
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List 
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        if len(nums)<4:
            return res
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2) :
                left=j+1
                right=len(nums)-1
                while left<right:
                    ident=nums[i]+nums[left]+nums[j]+nums[right]
                    if ident==target:
                        tmp=[nums[i],nums[left],nums[right],nums[j]]
                        if tmp not in res:
                            res.append(tmp)
                        right-=1
                    elif ident<target:
                        left+=1
                    else:
                        right-=1
        return res


soluton=Solution()
print(soluton.fourSum([1,0,-1,0,-2,2],0))


