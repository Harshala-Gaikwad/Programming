# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        p = head
        s=""
        while(p.next!=None):
            s+=str(p.val)
            p = p.next
        s+=str(p.val)    
        #s="0b"+s
        res=int(s,2)
        return res
