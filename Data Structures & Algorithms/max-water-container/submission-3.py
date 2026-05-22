class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1  # set right to last index
        max_area = 0

        while left < right:
            width = right - left
            h = min(heights[left], heights[right])
            area = width * h
            if area > max_area:
                max_area = area

            # Move the pointer at the shorter bar
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area