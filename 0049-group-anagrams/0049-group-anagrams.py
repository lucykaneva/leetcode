from collections import Counter
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        unique = {}
        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            if unique.get(key) is None:
                unique[key] = [] 
            unique[key].append(strs[i])
        return list(unique.values())
            
        

        