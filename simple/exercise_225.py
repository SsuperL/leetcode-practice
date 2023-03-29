"""
请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。

实现 MyStack 类：

void push(int x) 将元素 x 压入栈顶。
int pop() 移除并返回栈顶元素。
int top() 返回栈顶元素。
boolean empty() 如果栈是空的，返回 true ；否则，返回 false

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/implement-stack-using-queues
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import queue


class MyStack:
    def __init__(self):
        # 队列先进先出，队尾进队头出
        # 其中一个队列只用作备份
        self.queue_1 = queue.Queue()
        self.queue_2 = queue.Queue()

    def push(self, x: int) -> None:
        """将元素压入栈顶"""
        self.queue_1.put(x)

    def pop(self) -> int:
        """弹出栈顶元素"""
        # 出列从队列1中获取元素
        # 队列2用于备份，队列1的最后一个元素即为栈顶元素，弹出元素后交换两个队列即可
        # 其实一个队列即可实现栈
        while self.queue_1.qsize() > 1:
            self.queue_2.put(self.queue_1.get())

        res = self.queue_1.get()
        self.queue_1, self.queue_2 = self.queue_2, self.queue_1
        return res

    def top(self) -> int:
        """获取栈顶元素"""
        res = self.pop()
        self.queue_1.put(res)

        return res

    def empty(self) -> bool:
        """判断栈是否为空"""
        return self.queue_1.qsize() == 0


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())
print(obj.pop())
print(obj.empty())
