class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i,j]
        '''
        prev = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in prev:
                return [prev[diff],i]
            else:
                prev[num] = i