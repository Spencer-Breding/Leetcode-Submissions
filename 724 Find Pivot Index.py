# Runtime: 28ms (Beat 99.52% of submissions)
# Memory: 14.1 MB (Beat 19.18% of submissions)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        arr = []
        for n in nums:
            sum += n
            arr.append(sum)
        return arr
