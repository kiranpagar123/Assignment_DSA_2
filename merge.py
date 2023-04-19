class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_linked_lists_alternate(head1: ListNode, head2: ListNode) -> ListNode:
    current1 = head1
    current2 = head2
    while current1 and current2:
        temp = current1.next
        current1.next = current2
        current2 = current2.next
        current1.next.next = temp
        current1 = temp
    return head1

# Define the first linked list
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)

# Define the second linked list
head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(7)

# Merge the second linked list into the first linked list at alternate positions
merged_head = merge_linked_lists_alternate(head1, head2)

# Print the values of the modified linked list
current = merged_head
while current:
    print(current.val)
    current = current.next
