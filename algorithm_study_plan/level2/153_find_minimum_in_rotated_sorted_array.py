class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums= nums
        
        if len(nums)==1:
            return nums[0]
        return self.find_pivot(0, len(self.nums) -1)
        
        
    def find_pivot(self, low, high):
        if high< low:
            return self.nums[high]
        
        mid = (low + high) //2
        next_item =  float('inf')
        pre_item = float('inf')
        current = self.nums[mid]
        
        
        if (mid + 1) < len(self.nums):
            next_item =  self.nums[mid + 1]
        if (mid - 1) >= 0:
            pre_item =  self.nums[mid - 1]            
        
        if current < pre_item and current < next_item:
            return current
        
        if current < next_item and current < self.nums[high]:
            return self.find_pivot(low, mid -1)
        
        return self.find_pivot(mid + 1, high)
        
        