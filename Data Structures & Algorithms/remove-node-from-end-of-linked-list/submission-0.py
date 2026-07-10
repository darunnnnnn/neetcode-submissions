class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next

        if length == n:
            return head.next

        steps = length - n - 1

        curr = head

        while steps > 0:
            curr = curr.next
            steps -= 1

        curr.next = curr.next.next

        return head