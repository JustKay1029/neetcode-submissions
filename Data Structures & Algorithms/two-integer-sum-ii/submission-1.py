class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if target - numbers[i] in numbers:
                k = numbers.index(target- numbers[i])
                if k != i:
                    return [i+1, k+1]