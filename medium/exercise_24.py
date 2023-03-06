# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """标记三个节点"""
        res = ListNode(next=head)
        # 最左边的节点，设立虚拟头节点
        left = res
        while left.next and left.next.next:
            # 中间的节点
            mid = left.next
            # 最右边的节点
            right = left.next.next

            # 修改中间节点的next指针，指向实际的第二个节点的next节点
            mid.next = right.next
            # 修改最右边节点的next指针，指向实际的第一个节点，指向中间节点
            right.next = mid
            # 修改最左边节点（虚拟头节点）next指针，指向最右边节点
            left.next = right
            left = left.next.next

        return res.next


def print_node(head):
    while head:
        print(head.val)
        head = head.next


solution = Solution()

print_node(
    solution.swapPairs(
        ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4))))
    )
)
