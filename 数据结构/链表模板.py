# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 列表转链表
def list2link(List):
    head = ListNode(List[0])        # 创建一个头节点并将list第一个值赋值给头结点
    p = head                        # 创建头指针
    for i in range(1, len(List)):   # list从第二位开始遍历
        p.next = ListNode(List[i])  # 下一个结点p.next指向list值
        p = p.next                  # 指针往下移动
    return head                     # 返回头结点

# 链表打印
def link2print(head):
    while True:
        print(head.val, end='')
        head = head.next
        if head != None:
            print('->', end='')
        else:
            print('->NULL', end='')
            break

#
class Solution:
    def __init__(self):
        pass

    def function(self, head):
        pass

if __name__=='__main__':
    nums = [1, 2, 3, 4, 5]  # 1->2->3->4->5->NULL
    head = list2link(nums)
    # solution = Solution()
    # head = solution.function(head)
    link2print(head)