class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)

        maxL = [0]*n
        maxL[0] = (height[0])
        for i in range(1,n):
            maxL[i] = (max(maxL[i-1], height[i]))

        maxR = [0]*n
        maxR[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            maxR[i] = (max(maxR[i+1], height[i]))
        total = 0
        for i in range(0,n-1):
            total += max(0,min(maxL[i], maxR[i])-height[i])
        return total
