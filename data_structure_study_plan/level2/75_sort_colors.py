# URL: https://leetcode.com/problems/sort-colors/

# 75. Sort Colors

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
 

# Follow up: Could you come up with a one-pass algorithm using only constant extra space?

from collections import defaultdict
class Solution:

    # First Solution
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """        
        
        head= 0
        red_pointer= 0
        blue_pointer= len(nums)-1
        
        while head<=blue_pointer:
            
            if nums[head]==2:
                if nums[blue_pointer]==0:
                    nums[red_pointer]= 0
                    red_pointer += 1
                nums[blue_pointer]= 2
                blue_pointer-= 1
            
            elif nums[head]== 0:
                if nums[red_pointer]== 2:
                    nums[blue_pointer]=2
                    blue_pointer-= 1
                nums[red_pointer]= 0
                red_pointer+= 1
            print(nums)
            head+= 1
        
        for idx in range(red_pointer, blue_pointer):
            nums[idx]= 1

    # Second Solution
    def sortColors2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        red_pointer= 0
        white_pointer= 0
        blue_pointer= len(nums)-1
        
        while white_pointer<=blue_pointer:
            if nums[white_pointer] == 0:
                nums[white_pointer], nums[red_pointer]=  nums[red_pointer], nums[white_pointer]
                red_pointer+= 1
                white_pointer+= 1
            elif nums[white_pointer] == 2:
                nums[white_pointer], nums[blue_pointer]=  nums[blue_pointer], nums[white_pointer]
                blue_pointer-=1
            else:
                white_pointer+= 1