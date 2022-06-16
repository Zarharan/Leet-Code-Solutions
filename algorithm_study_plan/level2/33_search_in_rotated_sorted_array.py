class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1
        
        return self.binary_search(nums, target, 0, len(nums)-1)
        

    def binary_search(self, nums, target, low, high):
        if high < low:
            return -1            
        
        mid = (low + high)  // 2
        
        if nums[mid] == target:
            return mid           
        
        befor_item = nums[mid]
        next_item = nums[mid]
        if (mid -1) >= 0:
            befor_item = nums[mid-1]
            
        if (mid +1) < len(nums):
            next_item = nums[mid+1]
        
        
        
        if (nums[mid] < befor_item) and (target> nums[mid]) and (target> nums[high]):
            return self.binary_search(nums,target, low, mid-1)
        
        if (nums[mid] > next_item) and (target< nums[mid]) and (target< nums[low]):
            return self.binary_search(nums,target, mid + 1, high)
        
        left_target_index = self.binary_search(nums,target, low, mid-1)
        right_target_index = self.binary_search(nums,target, mid+1, high)
        return max(left_target_index, right_target_index)        
            