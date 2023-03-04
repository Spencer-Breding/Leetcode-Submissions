# Runtime: 23 ms (Beat 96.66% of submissions)
# Memory: 13.9 MB (Beat 48.83% of submissions)

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high+1)//2-low//2
