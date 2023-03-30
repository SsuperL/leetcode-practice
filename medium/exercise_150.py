"""
给你一个字符串数组 tokens ，表示一个根据 逆波兰表示法 表示的算术表达式。

请你计算该表达式。返回一个表示表达式值的整数。

注意：

有效的算符为 '+'、'-'、'*' 和 '/' 。
每个操作数（运算对象）都可以是一个整数或者另一个表达式。
两个整数之间的除法总是 向零截断 。
表达式中不含除零运算。
输入是一个根据逆波兰表示法表示的算术表达式。
答案及所有中间计算结果可以用 32 位 整数表示。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/evaluate-reverse-polish-notation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from operator import add
from operator import mul
from operator import sub
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 方法一： 使用eval，但比较慢
        stack = []
        for i in tokens:
            if i in ["+", "-", "*", "/"]:
                # 使用 int() 向零截断
                x = stack.pop()
                y = stack.pop()
                print(x, y)
                tmp = str(int(eval(f"{y}{i}{x}")))
                print(tmp)
                stack.append(tmp)
            else:
                stack.append(i)

        return int(stack[0])

    def evalRPN_2(self, tokens: List[str]):
        # 方法二：使用dict + stask
        stack = []
        op_map = {"+": add, "-": sub, "*": mul, "/": lambda x, y: int(x / y)}
        for i in tokens:
            if i in op_map:
                x, y = stack.pop(), stack.pop()
                tmp = op_map[i](int(y), int(x))
                stack.append(tmp)
            else:
                stack.append(int(i))
        return stack[0]


solution = Solution()
# print(solution.evalRPN(["2","1","+","3","*"]))
# print(solution.evalRPN(["4","13","5","/","+"]))
# ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
print(
    solution.evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
)
print(
    solution.evalRPN_2(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
)
print(solution.evalRPN_2(["4", "3", "-"]))
