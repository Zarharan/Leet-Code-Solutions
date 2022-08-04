# URL: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# 230. Kth Smallest Element in a BST

# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Example 1:

# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:

# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
 
# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 10**4
# 0 <= Node.val <= 10**4
 
# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Runtime: 45 ms, faster than 99.02% of Python3 online submissions for Kth Smallest Element in a BST.
    # Memory Usage: 17.9 MB, less than 89.14% of Python3 online submissions for Kth Smallest Element in a BST.
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.inorder_nodes=[]
        self.k = k
        
        self.inorder_traversal(root)
        
        return self.inorder_nodes[k-1]
        
    
    def inorder_traversal(self, root):
        
        if not root:
            return
        
        if len(self.inorder_nodes) >= self.k:
            return
        
        self.inorder_traversal(root.left)
        self.inorder_nodes.append(root.val)
        self.inorder_traversal(root.right)
        