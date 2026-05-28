class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if target - numbers[i] in numbers:
                k = numbers.index(target- numbers[i])
                if k != i:
                    return [i+1, k+1]
'''
For each index i, you check target - numbers[i] in numbers, 
which is an O(n) operation.

Then you call numbers.index(...), which is another 
O(n) operation.

Wrapped inside the for loop, this makes the overall time complexity roughly 
O(n**2).

It still passes because constraints are small enough here, 
but you are not using the fact that the array is sorted, 
and on larger constraints this pattern would be too slow
'''