"""
设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val和next。val是当前节点的值，next是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性prev以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。

在链表类中实现这些功能：

get(index)：获取链表中第index个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为val的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第index个节点之前添加值为val 的节点。如果index等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
deleteAtIndex(index)：如果索引index 有效，则删除链表中的第index 个节点。
"""


class MyLinkedList:
    def __init__(self):
        self.val = None
        self.next = None
        self.len = 0
        self.head = None

    def get(self, index: int) -> int:
        if index < 0 or index >= self.len:
            return -1
        cur = self.head
        while index:
            cur = cur.next
            index -= 1

        return cur.val

    def addAtHead(self, val: int) -> None:
        cur = self.head
        tmp = MyLinkedList()
        tmp.val = val
        tmp.next = cur
        self.len += 1
        self.head = tmp

    def addAtTail(self, val: int) -> None:
        cur = self.head
        if self.len == 0:
            self.addAtHead(val)
            return
        while cur.next:
            cur = cur.next

        tmp = MyLinkedList()
        tmp.val = val
        cur.next = tmp
        self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # index = 0特殊情况
        if index <= 0:
            self.addAtHead(val)
            return
        cur = self.head
        if index == self.len:
            self.addAtTail(val)
        else:
            while index - 1:
                cur = cur.next
                index -= 1
            tmp = MyLinkedList()
            tmp.val = val
            tmp.next = cur.next
            cur.next = tmp
            self.len += 1

    def deleteAtIndex(self, index: int) -> None:
        # index = 0特殊情况
        cur = self.head
        if index == 0 and self.len > 0:
            self.head = self.head.next
            self.len -= 1

        if index > 0 and index < self.len:
            while index - 1:
                cur = cur.next
                index -= 1

            cur.next = cur.next.next

            self.len -= 1
