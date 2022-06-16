class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        max_sum = float('-inf')
        current_sum = 0
        
        for num in nums:
            if num + current_sum > 0:
                current_sum += num
                max_sum = max(current_sum, max_sum)
            else:
                current_sum = 0
        
        if max_sum == float('-inf'):
            return max(nums)
        
        return max_sum