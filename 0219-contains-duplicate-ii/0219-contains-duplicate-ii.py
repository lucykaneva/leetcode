class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        elemIndex = {}
        for i in range(0, len(nums)):
            if nums[i] in elemIndex:
                if i - elemIndex[nums[i]]<=k:
                    return True
                else:
                    elemIndex[nums[i]]=i
            else:
                elemIndex[nums[i]]=i
        return False