"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        m=str(l1.val)
        n=str(l2.val)
        while l1.next or l2.next:
            if l1.next:
               l1=l1.next 
               m+=str(l1.val)
            if l2.next:
                l2=l2.next
                n+=str(l2.val)
        s=str(int(m[::-1])+int(n[::-1]))[::-1]
        t=ListNode(0)
        l=t

        for i in s:
            l.next=ListNode(int(i))
            l=l.next
        
        return t.next


solution=Solution()
res=solution.addTwoNumbers(ListNode(1,next=ListNode(4)),ListNode(2,next=ListNode(6)))
