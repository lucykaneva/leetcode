class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = dict()
        for num in nums:
            if num in map:
                map[num] = map[num] + 1
            else:
                map[num]=1
        for key in map.keys():
            if map[key]>len(nums)/2:
                return key

        