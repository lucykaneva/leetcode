class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        prereqsMap = {}
        safelyExplore = set()
        #queue
        discovered =set()
        for entry in prerequisites:
            if entry[0] in prereqsMap:
                prereqsMap[entry[0]].append(entry[1])
            else:
                prereqsMap[entry[0]] = []
                prereqsMap[entry[0]].append(entry[1])
        for i in range(0, numCourses):
            if (i in prereqsMap and not self.dfsHelper(prereqsMap, discovered, i, safelyExplore)):
                return False
        return True
        
    def dfsHelper(self, prereqsMap, discovered, currentEntry,safelyExplore):
        discovered.add(currentEntry)
        if currentEntry not in prereqsMap:
            #no prereqs
            discovered.remove(currentEntry)
            safelyExplore.add(currentEntry)
            return True
        for prereqs in prereqsMap[currentEntry]:
            if prereqs in discovered:
                return False
            if prereqs in safelyExplore:
                continue
            discovered.add(prereqs)
            if not self.dfsHelper(prereqsMap, discovered, prereqs, safelyExplore):
                return False
        discovered.remove(currentEntry)
        safelyExplore.add(currentEntry)
        return True
            
        

        
        