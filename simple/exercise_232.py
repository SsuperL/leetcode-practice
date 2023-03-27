"""
请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：

实现 MyQueue 类：

void push(int x) 将元素 x 推到队列的末尾
int pop() 从队列的开头移除并返回元素
int peek() 返回队列开头的元素
boolean empty() 如果队列为空，返回 true ；否则，返回 false
说明：

你 只能 使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/implement-queue-using-stacks
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class MyQueue:
    def __init__(self):
        # 一个用于进栈，一个用于出栈
        # 用于存放元素
        self.stack_1 = list()
        # 用于获取元素，没有元素则从第一个栈中获取
        self.stack_2 = list()

    def push(self, x: int) -> None:
        """元素入队列"""
        self.stack_1.append(x)

    def pop(self) -> int:
        """弹出队列第一个元素"""
        # 栈2中没有元素则从栈1中压入（所有元素）栈2再返回元素
        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
        return self.stack_2.pop()

    def peek(self) -> int:
        """获取队首元素"""
        # 栈2中没有元素则从栈1中压入（所有元素）栈2再返回元素
        res = self.pop()
        self.stack_2.append(res)
        return res

    def empty(self) -> bool:
        """判断队列是否为空"""
        return True if len(self.stack_1) + len(self.stack_2) == 0 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
q = MyQueue()
q.push(1)
q.push(2)
print(q.stack_2)
print(q.stack_1)
print(q.peek())
print(q.stack_2)
print(q.pop())
print(q.empty())
