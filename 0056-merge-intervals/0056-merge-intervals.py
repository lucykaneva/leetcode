class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals)==1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        i = 1
        output = [intervals[0]]
        while i < len(intervals):
            if output[-1][1]>=intervals[i][0]:
                new_list = [output[-1][0],max(intervals[i][1],output[-1][1])]
                output.pop()
                output.append(new_list)
            else:
                output.append(intervals[i])
            i+=1
        return output