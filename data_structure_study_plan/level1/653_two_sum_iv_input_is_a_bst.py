# URL: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

# Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.


# Example 1:


# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
# Example 2:


# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false
 

# Constraints:

# The number of nodes in the tree is in the range [1, 10**4].
# -10**4 <= Node.val <= 10**4
# root is guaranteed to be a valid binary search tree.
# -10**5 <= k <= 10**5

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.in_order_traversal = []
        self.in_order(root)
        
        head = 0
        tail = len(self.in_order_traversal) -1
        print(self.in_order_traversal)
        while head < tail:
            sum_2_item = self.in_order_traversal[head] + self.in_order_traversal[tail]
            if sum_2_item == k:
                return True
            elif sum_2_item > k:
                tail -= 1
            else:
                head += 1
                
        return False
        
        
    def in_order(self, node):
        if not node:
            return
        
        self.in_order(node.left)
        self.in_order_traversal.append(node.val)
        self.in_order(node.right)