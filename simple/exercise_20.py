"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isValid(self, s: str) -> bool:
        d = {")": "(", "}": "{", "]": "["}
        l = []
        for i in s:
            # 使用栈实现，如果栈不为空，且栈顶为左括号并与当前右括号匹配，则出栈，否则入栈
            if len(l) > 0 and i in d and d[i] == l[-1]:
                l.pop()
            else:
                l.append(i)
        return len(l) == 0


solution = Solution()
print(solution.isValid("([)]"))
