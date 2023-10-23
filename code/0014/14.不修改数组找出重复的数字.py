class Solution(object):
    def duplicateInArray(self, nums):
        """
        :type nums: List[int]
        :rtype int
        """
        l, r = 1, len(nums) - 1
        while l < r:
            s, mid = 0, l + r >> 1
            for num in nums:
                s += num >= l and num <= mid
            if s > mid - l + 1:
                r = mid
            else:
                l = mid + 1
        
        return l
