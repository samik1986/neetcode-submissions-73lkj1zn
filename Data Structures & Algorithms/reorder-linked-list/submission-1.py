class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        l2_rev = None
        curr = slow.next
        slow.next = None

        while curr:
            next_node = curr.next
            curr.next = l2_rev
            l2_rev = curr
            curr = next_node

        l1, l2 = head, l2_rev

        while l2:
            tmp1, tmp2 = l1.next, l2.next
            l1.next = l2
            l2.next = tmp1
            l1, l2 = tmp1, tmp2