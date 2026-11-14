class Solution:
    def longestPalindrome(self, s: str) -> int:
        dictCount = {}
        odd = False
        answ = 0
        for char in s:
            if char in dictCount:
                dictCount[char]+=1
            else:
                dictCount[char]=1
        for count in dictCount.values():
            if count%2 == 0:
                answ+=count
            else:
                odd = True
                answ += count-1
        return answ+1 if odd else answ
            

