class Solution(object):
    def searchArray(self, array, target):
        """
        :type array: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not array:
            return False
        
        n, m = len(array), len(array[0])
        i, j = 0, m - 1
        while i < n and j >= 0:
            if array[i][j] > target:
                j -= 1
            elif array[i][j] < target:
                i += 1
            else:
                return True
        
        return False
