# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        sm_ls = []
        lg_ls = []

        cnt = 0

        while head:
            if head.val < x:
                sm_ls.append(head)
            else:
                lg_ls.append(head)
            head = head.next
            cnt += 1

        for node in sm_ls:
            node.next = None

        for node in lg_ls:
            node.next = None
        
        for i in range(len(sm_ls)-1):
            node = sm_ls[i]
            next_node = sm_ls[i+1]
            node.next = next_node

        if sm_ls:   
            sm_ls[-1].next = lg_ls[0] if lg_ls else None

        for i in range(len(lg_ls)-1):
            node = lg_ls[i]
            next_node = lg_ls[i+1]
            node.next = next_node

        if lg_ls:
            lg_ls[-1].next = None

        if sm_ls:
            return sm_ls[0]
        elif lg_ls:
            return lg_ls[0]
        else: 
            return None