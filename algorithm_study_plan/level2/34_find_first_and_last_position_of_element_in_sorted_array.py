# Url: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 <= nums.length <= 10**5
# -109 <= nums[i] <= 10**9
# nums is a non-decreasing array.
# -109 <= target <= 10**9


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        
        target_index = self.binary_search(target, 0, len(nums) -1)
        
        if target_index == -1:
            return [-1,-1]
        
        # walk right
        right_index = target_index
        while ((right_index + 1) < len(nums) -1) and nums[target_index] == nums[right_index + 1]:
            right_index += 1

        # walk left
        left_index = target_index
        while ((left_index-1) >= 0) and nums[target_index] == nums[left_index - 1]:
            left_index -= 1            
            
        return [left_index, right_index]
    
    
    def binary_search(self, target, low, high):
        if high < low:
            return -1
        
        mid = high + low // 2
        
        if self.nums[mid] == target:
            return mid
        elif self.nums[mid] > target:
            return self.binary_search(target, low, mid -1)
        else:
            return self.binary_search(target, mid + 1, high)