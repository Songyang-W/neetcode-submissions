# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast,slow=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        secondhalf=None
        slowcopy=slow.next
        slow.next=None
        while slowcopy:
            temp=slowcopy.next
            slowcopy.next=secondhalf
            secondhalf=slowcopy
            slowcopy=temp
        firsthalf=head
        while secondhalf:
            tmp1,tmp2=firsthalf.next,secondhalf.next
            firsthalf.next=secondhalf
            secondhalf.next=tmp1
            firsthalf,secondhalf=tmp1,tmp2
        



        