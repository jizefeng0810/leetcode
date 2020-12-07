# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        fast, slow = head, head
        for i in range(n):
            fast = fast.next
        if fast == None: return head.next;
        while fast != None  and fast.next != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
