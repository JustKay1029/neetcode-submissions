from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []  # will store indices
        
        for i, temp in enumerate(temperatures):
            # Pop while current temp is warmer than the temp at top index
            while stack and temp > temperatures[stack[-1]]:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        
        return ans