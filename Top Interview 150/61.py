# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
            
        ls[left-1:right] = ls[left-1:right][::-1]
        dummy = ListNode(0)
        cur = dummy
        for node in ls:
            cur.next = ListNode(node)
            cur = cur.next
        return dummy.next