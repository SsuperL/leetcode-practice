"""
给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        res = head
        # if not head:
        #     return res
        # if not head.next:
        #     return head.next if head.val ==val else head
        while head:
            if not head.next:
                break
            if head.val == val:
                head = head.next
                res = head
                continue
            if head.next and head.next.val == val:
                head.next = head.next.next
                continue

            head = head.next

        return res


def print_node(head):
    while head:
        print(head.val)
        head = head.next


solution = Solution()
print_node(
    solution.removeElements(
        ListNode(
            1,
            ListNode(
                2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))
            ),
        ),
        val=6,
    )
)
print_node(
    solution.removeElements(
        ListNode(7, ListNode(7, ListNode(7, ListNode(7, ListNode())))), 7
    )
)
print_node(solution.removeElements(ListNode(6, ListNode()), 6))
print_node(solution.removeElements(ListNode(0, ListNode()), 1))
print_node(
    solution.removeElements(ListNode(1, ListNode(2, ListNode(2, ListNode(1)))), 2)
)
