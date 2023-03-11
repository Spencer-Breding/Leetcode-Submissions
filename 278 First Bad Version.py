# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        upper = n
        lower = 1
        while lower < upper:
            mid = (upper+lower)//2
            if isBadVersion(mid):
                upper=mid
                continue
            lower = mid+1
        return lower
