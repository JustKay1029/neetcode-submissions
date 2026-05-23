class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        from collections import defaultdict
    
        anagram_map = defaultdict(list)
    
        for s in strs:
        # Sort characters to create a key - anagrams have same sorted key
            key = ''.join(sorted(s))
            anagram_map[key].append(s)
    
        return list(anagram_map.values())
