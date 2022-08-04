# URL: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# 108. Convert Sorted Array to Binary Search Tree

# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

# Example 1:

# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:

# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

# Constraints:

# 1 <= nums.length <= 10**4
# -10**4 <= nums[i] <= 10**4
# nums is sorted in a strictly increasing order.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Runtime: 129 ms, faster than 50.89% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
    # Memory Usage: 15.6 MB, less than 83.29% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def bst_helper(low, high):
            
            if high< low:
                return None
            
            mid = (high + low) // 2
            
            current_node= TreeNode(nums[mid])
            current_node.left= bst_helper(low, mid-1)
            current_node.right= bst_helper(mid+1, high)
            
            return current_node
            
                    
        root= bst_helper(0, len(nums) -1)
        return root