# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return head
        prev = head
        curr = head.next
        prev.next = None
        temp = None
        while curr is not None:
            temp=curr
            curr=curr.next
            temp.next = prev
            prev = temp
        return prev

            
        