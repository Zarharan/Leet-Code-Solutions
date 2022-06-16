class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        for row in matrix:
            if row[0]>target:
                return False
            if self.binary_search(row, target, 0, len(row)-1):
                return True
            
        return False
        
    def binary_search(self, nums, target, low, high):
        if high< low:
            return False
        
        mid = (low+high)//2
        
        if nums[mid] == target:
            return True
        
        if nums[mid] < target:
            return self.binary_search(nums, target, mid+1, high)
        
        return self.binary_search(nums, target, low, mid - 1)