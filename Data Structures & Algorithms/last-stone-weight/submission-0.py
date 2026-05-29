import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Build max-heap by pushing negative values
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            # Pop two heaviest stones
            y = -heapq.heappop(max_heap)  # heaviest
            x = -heapq.heappop(max_heap)  # second heaviest
            
            if x != y:
                # Push the remaining stone (y - x) back
                heapq.heappush(max_heap, -(y - x))
        
        # If no stones left, return 0
        return -max_heap[0] if max_heap else 0