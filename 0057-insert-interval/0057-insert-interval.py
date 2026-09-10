class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        i = 0
        nISt= newInterval[0]
        nIEnd = newInterval[1]
        arrays = []
        incorporated = False
        if len(intervals)==0:
            arrays.append(newInterval)
            return arrays
        i = 0
        while i < len(intervals):
            if nIEnd < intervals[i][0] and not incorporated:
                arrays.append(newInterval)
                incorporated = True
            elif nISt > intervals[i][1] or nIEnd < intervals[i][0]:
                arrays.append(intervals[i])
                i+=1
            else:
                #start between end and start of the curr interval
                j = i
                incorporated = True
                while j < len(intervals) and nIEnd >= intervals[j][0] :
                    j+=1
                    print(j)
                arrays.append([min(intervals[i][0], nISt), max(intervals[j-1][1],nIEnd)])
                i = j
        if not incorporated:
            arrays.append(newInterval)
        return arrays
    
        