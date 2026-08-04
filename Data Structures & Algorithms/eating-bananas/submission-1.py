import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        hi = max(piles)
        lo = 1
        ans = hi
        while lo <= hi:
            k = (hi + lo) // 2
            # Calculate total hours needed at speed k
            total_hours = sum(math.ceil(pile / k) for pile in piles)
            if total_hours <= h:
                ans = k
                hi = k - 1
            else:
                lo = k + 1
        return ans