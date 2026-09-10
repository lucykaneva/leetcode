"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head==None:
            return None
        #set next
        current = head
        while current != None:
            currentCopy = Node(current.val, current.next, None)
            current.next = currentCopy
            current = current.next
            current = current.next
        current = head
        #set random
        while current != None:
            if current.next != None:
                if current.random == None:
                    current.next.random = None
                else:
                    current.next.random = current.random.next
            current = current.next
            current = current.next
        
        #unweave

        current = head
        copyHead = current.next
        copyCurrent = copyHead
        while copyCurrent != None:
            if current.next != None:
                current.next = current.next.next
            else:
                break
            if copyCurrent.next != None:
                copyCurrent.next = copyCurrent.next.next
            else:
                break
           
            copyCurrent = copyCurrent.next
            current = current.next
        return copyHead
        
        

            
            
        