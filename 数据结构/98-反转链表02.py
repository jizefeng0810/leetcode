# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def list2link(List):
    head = ListNode(List[0])        # 创建一个头节点并将list第一个值赋值给头结点
    p = head                        # 创建头指针
    for i in range(1, len(List)):   # list从第二位开始遍历
        p.next = ListNode(List[i])  # 下一个结点p.next指向list值
        p = p.next                  # 指针往下移动
    return head                     # 返回头结点

class Solution:
    """
        反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
    """
    def __init__(self):
        self.successor = None

    def reverseN(self, head, n):
        if n == 1:
            self.successor = head.next
            return head
        last = self.reverseN(head.next, n-1)
        head.next.next = head
        head.next = self.successor
        return last

    def reverseBetween(self, head, m, n) -> ListNode:
        if m == 1: return self.reverseN(head, n)
        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head

if __name__=='__main__':
    nums = [1, 2, 3, 4, 5]
    m, n = 2, 4             # 1->4->3->2->5->NULL
    head = list2link(nums)
    solution = Solution()
    head = solution.reverseBetween(head, m, n)
    while 1:
        print(head.val, end='')
        head = head.next
        if head != None:
            print('->', end='')
        else:
            print('->NULL', end='')
            break
