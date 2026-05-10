from itertools import combinations
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            ls = [ch for ch in s]
            lt = [ch for ch in t]
            return sorted(ls) == sorted(lt)