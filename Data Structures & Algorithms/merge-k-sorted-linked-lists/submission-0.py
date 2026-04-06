# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(0)
        cur = res

        while True:
            minListIdx = -1
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if minListIdx == -1 or lists[minListIdx].val > lists[i].val:
                    minListIdx = i
            
            if minListIdx == -1:
                break
            
            cur.next = lists[minListIdx]
            lists[minListIdx] = lists[minListIdx].next
            cur = cur.next

        return res.next