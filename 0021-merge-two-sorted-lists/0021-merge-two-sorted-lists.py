# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        first = 0
        second = 0
        curr1 = list1
        curr2 = list2
        current = None
        dummy = ListNode(-1)
        root = None
        while curr1 != None or curr2!=None:
            if current == None:
                current = dummy
            if curr1==None:
                current.next = curr2
                break
            if curr2 == None:
                current.next = curr1
                break
            if curr1!=None and curr2!=None:
                if curr1.val < curr2.val:
                        current.next = curr1
                        curr1 = curr1.next
                else:
                    current.next = curr2
                    curr2 = curr2.next
                current=current.next
        return dummy.next

        