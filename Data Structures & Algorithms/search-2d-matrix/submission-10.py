class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lst_1d = [item for sublist in matrix for item in sublist]
        return target in lst_1d
                
