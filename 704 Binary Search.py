class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = 0
        low = 0
        high = len(nums)-1
        while(low<=high):
            mid = (low+high)//2
            if(target==nums[mid]):
                return mid
            else:
                if(nums[mid]>target):
                    high = mid-1
                else:
                    low = mid+1
        return -1
