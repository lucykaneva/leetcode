# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        slow = head

        fast = head.next

        while fast != None and fast != slow:
            slow = slow.next
            if fast.next == None:
                return False
            fast = fast.next.next
        if fast == None:
            return False
        return True
        