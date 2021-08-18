# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        p = l3
        
        while True:
            if l1 is None and l2 is None:
                break
            elif l2 is None:
                p.next = l1
                break
            elif l1 is None:
                p.next = l2
                break
            else:
                S_val = 0
                if l1.val<l2.val:
                    S_val = l1.val
                    l1 = l1.next
                else:
                    S_val = l2.val
                    l2 = l2.next
                new_node = ListNode(S_val)
                p.next = new_node
                p = p.next
        return l3.next        
