class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums,target)
        """
        l,r = 0,len(nums)-1
        while l <= r:
            m = l+(r-l)//2
            if nums[m] > target: r -= 1
            elif nums[m] < target: l += 1
            else: return m
        return l
        """
        