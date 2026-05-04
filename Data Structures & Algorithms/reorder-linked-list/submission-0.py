# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s,f=head,head 
        while f and f.next :
            s=s.next 
            f=f.next.next 

        scnd=s.next 
        prev=s.next=None 
        while scnd:
            temp=scnd.next 
            scnd.next=prev 
            prev=scnd 
            scnd=temp 
        l1,l2=head,prev 
        while l2 :
            temp1,temp2 = l1.next,l2.next
            l1.next=l2 
            l2.next=temp1 
            l1,l2=temp1,temp2 














