class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr and curr.next:
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = curr
            prev.next = nxt
            prev = curr
            curr = curr.next
        return dummy.next
