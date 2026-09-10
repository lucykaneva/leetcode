class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers)-1
        answer=[]
        while i < j:
            if numbers[i] + numbers[j] == target:
                answer.append(i+1)
                answer.append(j+1)
                return answer
            if numbers[i] + numbers[j] < target:
                i+=1
            elif numbers[i] + numbers[j] > target:
                j-=1
        