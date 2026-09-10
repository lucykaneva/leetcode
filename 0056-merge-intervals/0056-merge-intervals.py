class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals)==1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        i=0
        output = []
        lastIndexOutput = -1
        while i < len(intervals):
            lastIndexOutput = len(output)-1
            if lastIndexOutput==-1 and i+1<len(intervals):
                intervOut = self.overlap(intervals[i], intervals[i+1])
            else:
                intervOut = self.overlap(intervals[i], output[lastIndexOutput])
            if intervOut and lastIndexOutput==-1:
                output.append(intervOut)
                i+=2
            elif intervOut:
                output[lastIndexOutput] = intervOut
                i+=1
            else:
                output.append(intervals[i])
                i+=1
        return output
    def overlap(self,arr1, arr2):
        if arr1[0]>=arr2[0] and arr1[1]<=arr2[1]:
            return [arr2[0],arr2[1]]
        if arr2[0]>=arr1[0] and arr2[1]<=arr1[1]:
            return [arr1[0],arr1[1]]
        if arr1[1] <= arr2[1] and arr1[1]>=arr2[0]:
            return [arr1[0], arr2[1]]
        if arr2[1] <= arr1[1] and arr2[1]>=arr1[0]:
            return [arr2[0], arr1[1]]
        return None         