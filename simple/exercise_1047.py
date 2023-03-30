"""
给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。

在 S 上反复执行重复项删除操作，直到无法继续删除。

在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        """使用栈实现，类似括号匹配"""
        stack = []
        for i in s:
            if len(stack) > 0 and i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)

        return "".join(stack)

        # 方法二： 双指针，快慢指针
        # 类似退格符

    def removeDuplicates_2(self, s: str):
        l = list(s)
        slow = fast = 0
        while fast < len(l):
            # 如果相同则使用fast对应的值替换slow对应的值，即将后面没有重复的元素移至前面
            l[slow] = l[fast]
            if slow > 0 and l[slow] == l[slow - 1]:
                if slow > 0:
                    slow -= 1
            else:
                slow += 1
            fast += 1
        return "".join(l[:slow])


solution = Solution()
print(solution.removeDuplicates_2("abbaca"))
print(solution.removeDuplicates_2("azxxzy"))
