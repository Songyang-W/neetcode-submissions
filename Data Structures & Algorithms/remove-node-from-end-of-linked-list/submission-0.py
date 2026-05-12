# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        fastpointer=head
        slowpointer=dummy
        while n>0:
            fastpointer=fastpointer.next
            n-=1
        while fastpointer:
            slowpointer=slowpointer.next
            fastpointer=fastpointer.next
        slowpointer.next=slowpointer.next.next

        return dummy.next

