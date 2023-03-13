"""
求环形链表的入口
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    设置快慢两个指针，快指针每次走两个节点，慢指针每次走一个节点，
    如果存在环，两个指针一定会在环内相遇
    """

    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # 如果相遇
            if slow == fast:
                p = head
                q = slow
                while p != q:
                    p = p.next
                    q = q.next
                # 也可以return q
                return p

        return ListNode()
