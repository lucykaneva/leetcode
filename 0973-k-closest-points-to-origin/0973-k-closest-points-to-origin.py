from heapq import heappop, heappush, heapify


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        h = []
        heapify(h)
        mapp = {}
        for i in range(0, len(points)):
            euclidianNeg = -1*self.getEuclidian(points[i][0], points[i][1])
            if len(h)<k:
                heappush(h,(euclidianNeg, points[i]))
            elif h[0][0] < euclidianNeg:
                heappop(h)
                heappush(h,(euclidianNeg, points[i]))

        output = []
        for i in range(0,k):
            output.append(heappop(h)[1])
        return output


    def getEuclidian(self,x,y):
        return math.sqrt(x*x + y*y)
  
        