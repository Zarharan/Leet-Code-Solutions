# url: https://leetcode.com/problems/squares-of-a-sorted-array/

# 977. Squares of a Sorted Array

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 

# Constraints:

# 1 <= nums.length <= 10**4
# -10**4 <= nums[i] <= 10**4
# nums is sorted in non-decreasing order.
 

# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        if len(nums)==1:
            return [nums[0]*nums[0]]
        
        head= 0
        tail= len(nums)-1
        square_nums = [0] * len(nums)
        square_nums_tail = tail

        while head <= tail:
            tail_square = pow(nums[tail], 2)
            head_square = pow(nums[head], 2)

            if tail_square >= head_square:
                square_nums[square_nums_tail] = tail_square
                tail -=1
            else:
                square_nums[square_nums_tail] = head_square
                head += 1
            
            square_nums_tail -= 1
                       
        return square_nums