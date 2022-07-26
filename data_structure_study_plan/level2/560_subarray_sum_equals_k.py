# URL: https://leetcode.com/problems/subarray-sum-equals-k/

# 560. Subarray Sum Equals K

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 2 * 10**4
# -1000 <= nums[i] <= 1000
# -10**7 <= k <= 10**7


from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sum_dict= defaultdict(int)
        sum_dict[0] = 1
        
        counter= 0
        total_sum= 0
        for num in nums:
            total_sum += num
            
            counter += sum_dict[total_sum-k]
            
            sum_dict[total_sum] += 1            
                
        return counter
                