class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        pref = []
        suf = []
        out = []
        n = len(nums)
        for i in range(n):
            pref.append(prefix)
            prefix *= nums[i]
        for i in range(n-1,-1,-1):
            suf.insert(0,suffix)
            suffix *= nums[i]
        for i in range(n):
            out.append(pref[i]*suf[i])
        return out
        