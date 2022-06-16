# Url: https://leetcode.com/problems/3sum/

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:

# Input: nums = []
# Output: []
# Example 3:

# Input: nums = [0]
# Output: []
 

# Constraints:

# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105


from collections import defaultdict
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
                
        if len(nums)<3:
            return []                       
    
        nums.sort()
        result = set()
        
        for idx, num in enumerate(nums):
            head = idx + 1
            tail = len(nums)-1
            
            while head < tail:
                sum_3 = num + nums[head] + nums[tail]
                if sum_3 == 0:
                    result.add((num, nums[head], nums[tail]))
                    head += 1
                    tail -= 1
                elif sum_3>0:
                    tail -= 1
                else:
                    head += 1
        
        return [list(i) for i in result]