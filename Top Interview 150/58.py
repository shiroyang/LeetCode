# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            tmp = val1 + val2 + carry
            carry = tmp // 10
            new = ListNode(tmp%10)
            cur.next = new
            cur = new
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

