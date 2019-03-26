class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = ListNode(0)
        p = l1
        q = l2
        carry = 0
        current_node = node
        while p is not None or q is not None:
            p_val = p.val if p is not None else 0
            q_val = q.val if q is not None else 0
            val_sum = carry + p_val + q_val
            carry = val_sum // 10
            current_node.next = ListNode(val_sum % 10)
            current_node = current_node.next
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next
        if carry > 0:
            current_node.next = ListNode(carry)

        return node.next
