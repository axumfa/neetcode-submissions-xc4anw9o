# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # first thoughhts just merging two linked list 
        if len(lists) == 0: return None
        if len(lists) == 1: return lists[0]
        k = 0
        
        while k < len(lists) - 1: 
            cur, nxt = lists[k], lists[k+1]
            # just incase it is dummy node
            dummy = ListNode()
            res = dummy
        

            while cur and nxt:
                if cur.val > nxt.val:
                    res.next = nxt
                    nxt = nxt.next
                else:
                    res.next = cur
                    cur = cur.next
                
                res = res.next
            
            # if element left
            if cur:
                res.next = cur
            if nxt:
                res.next = nxt
        
            
            lists[k + 1] = dummy.next
            k += 1
        
        return lists[k]


