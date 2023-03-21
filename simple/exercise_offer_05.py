"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
"""


class Solution:
    def replaceSpace(self, s: str) -> str:
        # 方法一：额外数组空间+双指针遍历替换
        # left,right = 0,len(s)-1
        # s_list = list(s)
        # new = "%20"
        # while left <= right:
        #     if s_list[left]==' ':
        #         s_list[left]=new
        #     if s_list[right]==' ':
        #         s_list[right]=new
        #     left+=1
        #     right-=1
        #
        # return "".join(s_list)

        # 方法二：在数组基础上扩充空间用于存储%20
        count = 0
        s_list = list(s)
        for i in s:
            # 统计空格个数
            if i == " ":
                count += 1
        # 由于python不能修改字符串，只能使用额外数组的方式
        # 扩充数组空间，一个空格扩充两个位置（空格原本有一个位置）用于存储%20
        s_list.extend([" "] * count * 2)
        # 双指针，从后往前填充
        left, right = len(s) - 1, len(s_list) - 1
        while left >= 0:
            if s_list[left] != " ":
                s_list[right] = s_list[left]
                left -= 1
                right -= 1
            else:
                s_list[right] = "0"
                s_list[right - 1] = "2"
                s_list[right - 2] = "%"
                left -= 1
                right -= 3

        return "".join(s_list)


solution = Solution()
print(solution.replaceSpace(s="We are happy."))
