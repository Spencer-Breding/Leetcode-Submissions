class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        arr = []
        for n in nums:
            sum += n
            arr.append(sum)
        return arr
