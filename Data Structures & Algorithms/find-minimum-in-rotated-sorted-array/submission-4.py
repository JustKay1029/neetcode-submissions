class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0
        l,r = 0, len(nums)-1
        while l < r:
            if nums[l] < nums[r]:
                r -= 1
                ans = nums[l]
            elif nums[l] > nums[r]:
                l += 1
                ans = nums[r]
        return ans