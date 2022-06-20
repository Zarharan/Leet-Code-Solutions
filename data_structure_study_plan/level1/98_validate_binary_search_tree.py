# URL: https://leetcode.com/problems/validate-binary-search-tree/

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [2,1,3]
# Output: true
# Example 2:


# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 10**4].
# -2**31 <= Node.val <= 2**31 - 1


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # return self.validate_bst_brute_force(root)

        return self.validate_bst(root, float('-inf'), float('inf'))

    
    # This solution is optimum regarding space and time complexity.
    def validate_bst(self, node, left, right):
        
        if not node:
            return True
        
        if node.val <= left or node.val>= right:
            return False
        
        return self.validate_bst(node.left, left, node.val) and self.validate_bst(node.right, node.val, right)
        
    
    # This solution is not optimum regarding space complexity. The space Complexity is O(N) (N= number of nodes in the tree).
    def validate_bst_brute_force(self, node):
        self.values = []
        
        self.in_order(root)
        
        min_val = self.values[0]
        
        for item in self.values[1:]:
            if item<= min_val:
                return False
            
            min_val= item
        
        return True
    
        
    def in_order(self, root):
        if not root:
            return
        
        self.in_order(root.left)
        self.values.append(root.val)
        self.in_order(root.right)

        
        
        