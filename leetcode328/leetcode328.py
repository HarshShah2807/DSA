class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None: 
            return head
        odd=head
        even=head.next
        even_start=even
        while even!=None and even.next!=None:
            odd.next=even.next
            odd = odd.next
            even.next=odd.next
            even=even.next
        odd.next=even_start
        return head
