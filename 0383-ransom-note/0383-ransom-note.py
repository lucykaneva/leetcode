class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magsCount = {}
        for char in magazine:
            if char in magsCount:
                magsCount[char]+=1
            else:
                magsCount[char]=1
        for char in ransomNote:
            if char in magsCount:
                magsCount[char]-=1
                if magsCount[char]<0:
                    return False
            else:
                    return False
        return True
        