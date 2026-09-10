class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastPos = {}
        maxSeq = 1
        start = 0
        duplicates = False
        for i in range(0,len(s)):
            char = s[i]
            if char in lastPos:
                duplicates = True
                if i-start > maxSeq:
                    maxSeq = i-start
                start = max(lastPos[char]+1,start)
            lastPos[char] = i
        return max(maxSeq, len(s)-start) if duplicates else len(s)
            



        