# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ls = []

        while head:
            ls.append(head)
            head = head.next

        ls.pop(-n)

        if len(ls) == 0: return None
        if n == 1: ls[-1].next = None; return ls[0]

        for i in range(len(ls)-1):
            node = ls[i]
            next_node = ls[i+1]
            node.next = next_node
        
        return ls[0]