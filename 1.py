class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def merge_two_sorted_lists(l1, l2):
    dummy = ListNode()
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1
    if l2:
        current.next = l2

    return dummy.next

def insertion_sort_linked_list(head):
    dummy = ListNode(float('-inf'))
    dummy.next = head
    last_sorted = dummy.next

    while last_sorted.next:
        if last_sorted.next.val < last_sorted.val:
            prev = dummy
            while prev.next.val < last_sorted.next.val:
                prev = prev.next

            temp = last_sorted.next
            last_sorted.next = last_sorted.next.next
            temp.next = prev.next
            prev.next = temp
        else:
            last_sorted = last_sorted.next

    return dummy.next

def linked_list(head):
    if not head or not head.next:
        return head

    mid = get_middle(head)
    left = head
    right = mid.next
    mid.next = None

    left_sorted = linked_list(left)
    right_sorted = linked_list(right)

    return merge_two_sorted_lists(left_sorted, right_sorted)

def get_middle(head):
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(5)

l2 = ListNode(2)
l2.next = ListNode(4)
l2.next.next = ListNode(6)

merged_list = merge_two_sorted_lists(l1, l2)

while merged_list:
    print(merged_list.val, end=" ")
    merged_list = merged_list.next
