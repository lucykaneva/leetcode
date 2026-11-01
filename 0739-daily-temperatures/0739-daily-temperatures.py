class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        results = [0] * len(temperatures)
        stack = []                                   # indexes of days still waiting
        for i, today in enumerate(temperatures):
            while stack and today > temperatures[stack[-1]]:
                day = stack.pop()                    # this day just found its warmer day
                results[day] = i - day
            stack.append(i)                          # today waits for its own answer
        return results
