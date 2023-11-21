# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        from collections import defaultdict
        # {val1:{index1, index2 ...}}
        d = defaultdict(list)
        NodeList = []
        cnt = 0

        while head:
            d[head.val].append(cnt)
            NodeList.append(head)
            head = head.next
            cnt += 1

        ToBeDiscarded = [False]*(cnt+1)

        for key, index_ls in d.items():
            if len(index_ls) > 1:
                for index in index_ls:
                    ToBeDiscarded[index] = True

        for i in range(cnt, -1, -1):
            if ToBeDiscarded[i]:
                NodeList.pop(i)

        if len(NodeList) == 0: return None
        for node in NodeList:
            node.next = None
        for i in range(len(NodeList)-1):
            cur = NodeList[i]
            nxt = NodeList[i+1]
            cur.next = nxt
        
        return NodeList[0]