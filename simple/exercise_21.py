"""
合并两个有序单链表
"""
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode()
        p=res

        while list1 and list2:
            # 比较两个链表的值，并移动链表指针和目标链表指针
            if list1.val==list2.val:
                p.next=ListNode(list1.val)
                p=p.next
                p.next=ListNode(list2.val)
                p=p.next
                list1=list1.next
                list2=list2.next
            elif list1.val>list2.val:
                p.next=ListNode(list2.val)
                p=p.next
                list2=list2.next
            elif list1.val<list2.val:
                p.next=ListNode(list1.val)
                p=p.next
                list1=list1.next
        
        # 其中一个链表为空时，将指针指向另一链表
        if not list1:
            p.next=list2
        
        elif not list2:
            p.next=list1

        return res.next

solution=Solution()
res=solution.mergeTwoLists(ListNode(1,next=ListNode(2,next=ListNode(4))),ListNode(1,next=ListNode(3,next=ListNode(4))))
while res:
    print(res.val)
    res=res.next
