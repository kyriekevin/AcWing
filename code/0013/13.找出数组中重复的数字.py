class Solution(object):
    def duplicateInArray(self, nums):
        """
        :type nums: List[int]
        :rtype int
        """
        n = len(nums)
        for num in nums:
            if num < 0 or num > n - 1:
                return -1
        
        for i in range(n):
            while nums[nums[i]] != nums[i]:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            if nums[i] != i:
                return nums[i]
        
        return -1
