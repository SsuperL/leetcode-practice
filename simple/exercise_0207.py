"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

图示两个链表在节点 c1 开始相交：

来源：力扣（LeetCode）
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """注意是判断指针相同，不需要逐一判断结点值是否相等"""
        cur_a = headA
        cur_b = headB
        len_a = 0
        len_b = 0
        while cur_a:
            len_a += 1
            cur_a = cur_a.next
        while cur_b:
            len_b += 1
            cur_b = cur_b.next

        first = headA
        second = headB
        # 始终让len_b代表最长链表的长度
        if len_a > len_b:
            len_b, len_a = len_a, len_b
            second, first = first, second

        # 让两个链表处于同一起始位置
        for _ in range(len_b - len_a):
            second = second.next
        while first:
            # 只要结点指针相同就可以直接返回
            if first == second:
                return first

            first = first.next
            second = second.next

        return first


def print_node(node):
    while node:
        print(node.val)
        node = node.next


solution = Solution()
print_node(
    solution.getIntersectionNode(
        ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4)))),
        ListNode(5, next=ListNode(7, next=ListNode(3, next=ListNode(4)))),
    )
)
