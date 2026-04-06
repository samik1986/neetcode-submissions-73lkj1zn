class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        
        carry = 0
        while (l1!=None) | (l2!=None) :
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = val1 + val2 + carry
            carry, val = divmod(sum, 10)
            curr.next = ListNode(val)
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            curr = curr.next
        
        if carry: curr.next = ListNode(carry)

        return dummy.next