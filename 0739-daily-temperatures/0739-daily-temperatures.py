class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        results = [0] * len(temperatures)
        stack = []                                   # indexes of days still waiting
        for i in range(0,len(temperatures)):
            today = temperatures[i]
            if len(stack)==0:
                stack.append(i)
            else:
                lastIndex = stack[-1]
                while temperatures[lastIndex]<today and len(stack)>0:
                    results[lastIndex] = i-lastIndex
                    stack.pop()
                    if len(stack)>0:
                        lastIndex = stack[-1]
                stack.append(i)
        return results
