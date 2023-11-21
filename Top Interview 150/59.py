# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        while list1 or list2:
            val1 = list1.val if list1 else 10**16
            val2 = list2.val if list2 else 10**16
            if val1 <= val2:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        if not list1:
            while list2:
                cur.next = list2
                list2 = list2.next
        else:
            while list1:
                cur.next = list1
                list1 = list1.next
        return dummy.next