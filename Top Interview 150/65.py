# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        NodeList = []
        cnt = 0
        while head:
            NodeList.append(head)
            head = head.next
            cnt += 1
        
        if cnt == 0: return None
        k %= cnt

        NodeList = NodeList[-k:] + NodeList[:-k]

        for node in NodeList:
            node.next = None
        
        for i in range(len(NodeList)-1):
            node = NodeList[i]
            next_node = NodeList[i+1]
            node.next = next_node

        return NodeList[0] if NodeList else None
