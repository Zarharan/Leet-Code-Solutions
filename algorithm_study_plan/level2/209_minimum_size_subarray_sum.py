# Url: https://leetcode.com/problems/minimum-size-subarray-sum/

# Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.


# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
 

# Constraints:

# 1 <= target <= 10**9
# 1 <= nums.length <= 10**5
# 1 <= nums[i] <= 10**5
 

# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 1:
            if nums[0] < target:
                return 0
            return 1
        
        head = 0
        total_sum = 0
        min_len = 0
        
        for i in range(len(nums)):
            total_sum += nums[i]
            
            while total_sum >= target and head<i:
                total_sum -= nums[head]
                if total_sum<target:
                    total_sum += nums[head]
                    break
                
                head +=1
            
            if total_sum >= target:
                if min_len == 0:
                    min_len = (i-head) + 1
                min_len = min(min_len, (i-head) + 1)
                
        return min_len
            