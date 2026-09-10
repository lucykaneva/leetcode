class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        lastIndex=len(nums)-1
        k=0
        i=0
        while i <= lastIndex:
            if nums[i] != val:
                k+=1
                i+=1
            else:
                temp=nums[lastIndex]
                nums[lastIndex]= nums[i]
                nums[i] = temp
                lastIndex-=1
        return k