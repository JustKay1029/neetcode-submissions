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
'''
In this solution I first created a single output array | list which firstly had prefixes
and then i iterated from right to left while multiplying every element 
at the correct index
'''