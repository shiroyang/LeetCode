# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        node = []
        cur = head
        while cur:
            node.append(cur)
            cur = cur.next

        n = len(node)
        l = 0
        r = n-1
        ans = -10**16

        while l < r:
            ans = max(ans, node[l].val+node[r].val)

            l += 1
            r -= 1

        return ans


