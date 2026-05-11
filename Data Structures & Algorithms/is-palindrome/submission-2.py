class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip()
        clean = ""
        for c in s:
            if c.isalnum():
                clean += c
        return clean == clean[::-1]