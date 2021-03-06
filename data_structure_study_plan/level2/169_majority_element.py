# URL: https://leetcode.com/problems/majority-element/

# 169. Majority Element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 10**4
# -10**9 <= nums[i] <= 10**9
 

# Follow-up: Could you solve the problem in linear time and in O(1) space?


from collections import defaultdict
class Solution:
    # Solution 1
    # Time complexity= O(n) and space complexity= O(n)
    def majorityElement(self, nums: List[int]) -> int:
        num_count = defaultdict(int)
        
        for num in nums:
            num_count[num] += 1
        
        biggest= 0
        result = 0
        for num, counter in num_count.items():            
            if biggest< counter:
                biggest= counter
                result = num
            
        return result

    # Solution 2
    # Time complexity= O(n) and space complexity= O(1)
    def majorityElement2(self, nums: List[int]) -> int:
        
        counter= 0
        majority_item= 0
        
        for num in nums:
            if counter== 0:
                majority_item= num
            
            counter += 1 if (num==majority_item) else -1
            
        return majority_item