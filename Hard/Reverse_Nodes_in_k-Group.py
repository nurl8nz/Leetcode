class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head
        
        while True:
            count = 0
            temp = curr
            while temp and count < k:
                temp = temp.next
                count += 1
            if count < k:
                break
            
            prev_next, tail = prev.next, curr
            for _ in range(k):
                nxt = curr.next
                curr.next = prev.next
                prev.next = curr
                curr = nxt
            
            tail.next = curr
            prev = tail
        
        return dummy.next
