class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        out = []
        n = len(nums)
        for i in range(n):
            out.append(prefix)
            prefix *= nums[i]
        for i in range(n-1,-1,-1):
            out[i] *= suffix
            suffix *= nums[i]
        return out
        