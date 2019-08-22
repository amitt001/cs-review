class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseKGroup(head, k: int):
    current = head
    next = prev = None
    new_head = None
    last_prev = None
    ll_len = 0
    tmp = head
    while tmp:
        ll_len += 1
        tmp = tmp.next

    while current:
        start = None
        counter = 0
        prev = None
        if ll_len < k:
            if last_prev:
                last_prev.next = current
            break
        while current and counter < k:
            if start is None:
                start = current
            next = current.next
            current.next = prev
            prev = current
            current = next
            counter += 1
            ll_len -= 1

        if new_head is None:
            new_head = prev

        if last_prev:
            last_prev.next = prev
        last_prev = start

    return new_head or head


if __name__ == '__main__':
    head = ListNode(1)
    head.next  = ListNode(2)
    head.next.next  = ListNode(3)
    head.next.next.next  = ListNode(4)
    head.next.next.next.next  = ListNode(5)
    head.next.next.next.next.next  = ListNode(6)
    head.next.next.next.next.next.next  = ListNode(7)
    head.next.next.next.next.next.next.next  = ListNode(8)
    node = reverseKGroup(head, 3)
    while node:
        print(node.val)
        node = node.next
