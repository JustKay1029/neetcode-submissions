# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        temp = head 
        if not head:
            return None
        while temp.next:
            stack.append(temp)
            temp = temp.next
        
        new = temp
        while stack:
            node = stack.pop()
            temp.next = node
            temp = node
        temp.next = None
        return new