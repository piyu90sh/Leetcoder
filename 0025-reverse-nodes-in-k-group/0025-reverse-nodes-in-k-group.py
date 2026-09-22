class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            curr = prev

            # Check if k nodes are available
            for i in range(k):
                curr = curr.next
                if curr is None:
                    return dummy.next

            # Reverse k nodes
            group_prev = prev
            group_next = curr.next

            curr = prev.next
            prev_node = group_next

            while curr != group_next:
                next_node = curr.next
                curr.next = prev_node
                prev_node = curr
                curr = next_node

            # Connect reversed group
            temp = prev.next
            prev.next = prev_node
            prev = temp