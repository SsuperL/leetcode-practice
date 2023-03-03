"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 使用双指针法，将翻转链表节点间的指向
        if not head or not head.next:
            return head
        cur = head
        pre = None
        tmp = None
        while cur.next:
            pre = ListNode(cur.val)
            pre.next = tmp
            tmp = pre
            pre = cur.next
            cur = cur.next

        pre.next = tmp
        return pre


def print_node(head):
    print("rrr", head.val)
    while head:
        print("zzz", head.val)
        head = head.next


solution = Solution()
print_node(
    solution.reverseList(
        ListNode(
            val=1,
            next=ListNode(
                val=2, next=ListNode(val=3, next=ListNode(4, next=ListNode(5)))
            ),
        )
    )
)
# 1->2->3->4->5

print(solution.reverseList([]))
