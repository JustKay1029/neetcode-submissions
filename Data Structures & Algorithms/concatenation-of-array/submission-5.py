class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n*2
        for i in range(n*2):
            if i >= n:
                ans[i] = nums[i-n] #ans = [1,] 
            else:
                ans[i] = nums[i]
        return ans