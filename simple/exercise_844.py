"""
给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 true 。# 代表退格字符。

注意：如果对空文本输入退格字符，文本继续为空。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/backspace-string-compare
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # res1 = ""
        # res2 = ""
        # for i in s:
        #     if i != "#":
        #         res1 += i
        #     else:
        #         res1 = res1[:-1]
        #
        # for j in t:
        #     if j != "#":
        #         res2 += j
        #     else:
        #         res2 = res2[:-1]
        #
        # if res1 == res2:
        #     return True
        # return False

        # 方法二：栈
        # 方法三：快慢指针
        def back(l):
            slow, fast = 0, 0
            while fast < len(l):
                if l[fast] == "#":
                    if slow > 0:
                        slow -= 1
                    fast += 1
                    continue
                l[slow] = l[fast]
                slow += 1
                fast += 1
            return slow

        data_1, data_2 = list(s), list(t)
        slow_1 = back(data_1)
        slow_2 = back(data_2)
        print(data_1, data_2)
        print(slow_1, slow_2)
        return data_1[:slow_1] == data_2[:slow_2]


solution = Solution()
# s, t = "xywrrmp", "xywrrm#p"
# print(solution.backspaceCompare(s, t))
s = "y#fo##f"
t = "y#f#o##f"
print(solution.backspaceCompare(s, t))
