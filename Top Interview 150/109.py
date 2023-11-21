# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_list = []
        while head:
            node_list.append(head)
            head = head.next

        node_list.sort(key=lambda x:x.val)

        for i in range(len(node_list)-1):
            node = node_list[i]
            next_node = node_list[i+1]

            node.next = next_node
        
        if node_list: node_list[-1].next = None
        return node_list[0] if node_list else None