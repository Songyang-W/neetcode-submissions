# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        newlist=ListNode(0)
        dummy=newlist

        while True:
            cur_sm=-1
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if cur_sm==-1 or lists[cur_sm].val>lists[i].val:
                    cur_sm=i
            if cur_sm==-1:
                return dummy.next

            newlist.next=lists[cur_sm]
            lists[cur_sm]=lists[cur_sm].next
            newlist=newlist.next

            
