class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        longest = 0
        
        values = sorted(count.values(), reverse=True)
        odd_present = False
        
        for value in values:
            if value % 2 == 0:
                longest += value
            else:
                longest += (value - 1)
                odd_present = True
        
        if odd_present:
            return longest + 1
        
        return longest
