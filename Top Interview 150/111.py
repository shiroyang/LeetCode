# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:   
        ans = []
        for head in lists:
            while head:
                ans.append(head)
                head = head.next
        
        ans.sort(key=lambda x:x.val)
        for i in range(len(ans)-1):
            node = ans[i]
            next_node = ans[i+1]
            node.next = next_node
        if ans: ans[-1].next = None
        return ans[0] if ans else None