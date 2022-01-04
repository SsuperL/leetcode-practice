"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l = []
        while head:
            l.append(head.val)
            head = head.next      
        l.pop(-n)
        res = ListNode()
        h = res
        for i in l:
            res.next = ListNode(i)
            res = res.next       
        return h.next
