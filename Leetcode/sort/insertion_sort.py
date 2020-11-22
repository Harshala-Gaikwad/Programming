# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        p = head
        q=ListNode()
        while(p):
            prev = q
            next_p = q.next
            while next_p:
                if p.val<next_p.val:
                    break
                prev = prev.next
                next_p = next_p.next
            temp = p.next
            
            p.next = next_p
            prev.next=p
            
            p = temp
        return q.next    
        
