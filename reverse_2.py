class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list_in_groups(head: ListNode, k: int) -> ListNode:
    current = head
    count = 0
    while current and count < k:
        current = current.next
        count += 1
    if count < k:
        return head
    current = head
    prev = None
    next_node = None
    count = 0
    while current and count < k:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        count += 1
    if next_node:
        head.next = reverse_linked_list_in_groups(next_node, k)
    return prev




# Define the linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Reverse the linked list in groups of size 3
new_head = reverse_linked_list_in_groups(head, 3)

# Print the values of the modified linked list
current = new_head
while current:
    print(current.val)
    current = current.next

