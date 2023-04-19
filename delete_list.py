class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def delete_zero_sum_sublists(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    prefix_sum = 0
    d = {prefix_sum: dummy}
    while head:
        prefix_sum += head.val
        d[prefix_sum] = head
        head = head.next
    prefix_sum = 0
    head = dummy
    while head:
        prefix_sum += head.val
        head.next = d[prefix_sum].next
        head = head.next
    return dummy.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
new_head = delete_zero_sum_sublists(head)
current = new_head
while current:
    print(current.val)
    current = current.next

