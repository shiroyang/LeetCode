# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 1
        cur = head
        ans = []
        while cur.next:
            cur = cur.next
            ans.append(cur.val)
            cnt += 1

        if cnt == 1:
            return None
        
        cur = head
        for _ in range(cnt//2-1):
            cur = cur.next
        
        cur.next = cur.next.next
        return head