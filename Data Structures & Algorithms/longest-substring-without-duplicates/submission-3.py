class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        l = 0
        seen = set()
        max_len = 0
        for r in range(len(s)):
            # While s[r] is a duplicate in our window, shrink from the left
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            # Now that the duplicate is gone, add the new character
            seen.add(s[r])
            # Calculate current window length and update max
            max_len = max(max_len, r - l + 1)
        return max_len