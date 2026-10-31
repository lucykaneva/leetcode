from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = Counter(nums)
        for num, c in counts.items():
            if c > len(nums) // 2:
                return num

        