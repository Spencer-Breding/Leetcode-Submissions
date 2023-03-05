# First Solution I came up with, not clean
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head):
            return head
        temp = []
        temp2 = tail = ListNode(None)
        while (head):
            temp.append(head.val)
            head = head.next
        temp.reverse()
        for i in temp:
            if(tail.val == None):
                temp2 = tail = ListNode(i)
                continue
            temp2.next = ListNode(i)
            temp2 = temp2.next
        return tail
        
        
        
# Cleaner Solution       
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            old = cur.next
            cur.next = prev
            prev = cur
            cur = old
        return prev
