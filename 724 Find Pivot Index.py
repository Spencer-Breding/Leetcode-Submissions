class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum=0
        rightSum=sum(nums)
        for i in range(len(nums)):
            rightSum -= nums[i]
            leftSum += nums[i]
            if (leftSum-nums[i]) == rightSum:
                return i
        return -1
