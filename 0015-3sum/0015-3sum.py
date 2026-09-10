class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        triples = []
        for i in range(0,len(nums)-2):
            x = nums[i]
            if i != 0 and nums[i] == nums[i-1]:
                continue
            k = i+1
            j = len(nums)-1
            while k < j:
                currentS = nums[k] + nums[j]
                if currentS == 0-x:
                    curr = [x, nums[k], nums[j]]
                    triples.append(curr)
                    k+=1
                    j-=1
                    while j>k and nums[j+1] == nums[j]:
                        j-=1
                    while j>k and nums[k-1] == nums[k]:
                        k+=1
                elif currentS > 0-x:
                    j-=1
                else:
                    k+=1
                    
                
        return triples