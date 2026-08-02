class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        
        while l < r:
            # Move left pointer if not alphanumeric
            while l < r and not s[l].isalnum():
                l += 1
            # Move right pointer if not alphanumeric
            while l < r and not s[r].isalnum():
                r -= 1
            
            # Compare characters
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
            
        return True