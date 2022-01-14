# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        l=head
        while l and l.next:
            l.val,l.next.val=l.next.val,l.val
            l =head.next.next
        return head
