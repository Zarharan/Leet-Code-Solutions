class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        self.last_index = len(nums) - 1
        
        if len(nums) == 1:
            return 0
        
        return self.find_peak_element(0, (len(nums) -1))
        
        
    def find_peak_element(self, low, high):
        if high<low:
            return -1
        
        mid = (low + high) // 2
        
        pre_item = float('-inf')
        next_item = float('-inf')
        
        if (mid - 1)>= 0:
            pre_item = self.nums[mid - 1]
            
        if (mid + 1)<=self.last_index:
            next_item = self.nums[mid + 1]            
        
        if (self.nums[mid] > next_item) and (self.nums[mid] > pre_item):
            return mid
        
        if next_item > pre_item:
            return self.find_peak_element(mid + 1, high)
        
        return self.find_peak_element(low, mid - 1)
            
            