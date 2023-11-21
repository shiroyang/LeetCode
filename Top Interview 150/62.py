# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Reverse k nodes
    # node1 -> node2 -> node3 -> None
    # next_node = node2, node1 -> None, new_head = node1, ptr = node2
    # node3 -> node2 -> node1 -> None
    def reverseLinkedList(self, head, k):
        new_head, ptr = None, head
        while k:
            next_node = ptr.next
            ptr.next = new_head
            new_head = ptr

            ptr = next_node

            k -= 1
        
        return new_head


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cnt = 0
        ptr = head

        while cnt < k and ptr:
            ptr = ptr.next
            cnt += 1

        if cnt == k:
            reversedHead = self.reverseLinkedList(head, k)
            head.next = self.reverseKGroup(ptr, k)
            return reversedHead
        return head