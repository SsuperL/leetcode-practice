"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        使用两个间隔为n的双指针，快指针先向前移动n+1步，接着快慢指针同时移动
        使用虚拟头节点，移动n+1步是因为头节点可能会被删除
        :param head:
        :param n:
        :return:
        """
        cur = ListNode(next=head)
        slow = cur
        fast = cur
        while n + 1:
            fast = fast.next
            n -= 1
        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return cur.next


def print_node(node):
    while node:
        print(node.val)
        node = node.next


solution = Solution()
print_node(
    solution.removeNthFromEnd(
        head=ListNode(1, next=ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), n=2
    )
)
print_node(solution.removeNthFromEnd(ListNode(1), 1))
