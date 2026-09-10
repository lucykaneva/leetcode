from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ctr = Counter(nums)
        common_list = ctr.most_common(k)
        list = []
        for common in common_list:
            list.append(common[0])
        return list
        