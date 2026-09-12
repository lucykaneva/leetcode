"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        frontier = []
        frontierSet = set()
        frontier.append(node)
        frontierSet.add(node)
        nodes = {}
        root = node
        while len(frontier)>0:
            node = frontier.pop()
            if node is not None:
                if node.val not in nodes:
                    

                    newNode = Node (node.val,[])
                    if len(nodes)==0:
                        root = newNode
                    nodes[newNode.val] = newNode
                    copyNode = newNode
                else:
                    copyNode = nodes[node.val]
                neighbors = node.neighbors
                for curr in neighbors:
                    if curr not in frontierSet:
                        frontier.append(curr)
                        frontierSet.add(curr)
                    if curr.val in nodes:
                        thisCopyNode = nodes[curr.val]
                        if thisCopyNode not in copyNode.neighbors:
                            copyNode.neighbors.append(thisCopyNode)
                        if copyNode not in thisCopyNode.neighbors:
                            thisCopyNode.neighbors.append(copyNode)
                    else:
                        newNode = Node (curr.val, [])
                        newNode.neighbors.append(copyNode)
                        copyNode.neighbors.append(newNode)
                        nodes[newNode.val] = newNode
        return root

                


