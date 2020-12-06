# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        """
            给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
        """
        if head == None or head.next == None: return None
        fast, slow = head, head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow: break
        if fast == None or fast.next == None: return None
        # 上面判断环形链表，下面找出初始位置

        slow = head
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return slow
