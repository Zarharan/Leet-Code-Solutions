# URL: https://leetcode.com/problems/reverse-nodes-in-k-group/

# 25. Reverse Nodes in k-Group

# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Example 1:

# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:

# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
 
# Constraints:

# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
 

# Follow-up: Can you solve the problem in O(1) extra memory space?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Runtime: 212 ms, faster than 76.73% of Python3 online submissions for Reverse Nodes in k-Group.
    # Memory Usage: 23.9 MB, less than 40.24% of Python3 online submissions for Reverse Nodes in k-Group.
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        tail= head.next
        
        if not tail or k==1:
            return head
        
        new_head= None
        pre_k_last_node= None
        
        while tail:
            
            # skip k nodes and then reverse these nodes
            first_node_in_current_k= head
            counter= 0
            for i in range(k-1):                
                if tail and head:
                    tail= tail.next
                    head= head.next
                    counter+= 1
                else:
                    break
                
            
            # if the number of remaining nodes is less than k, then these nodes should remain as they are
            if counter< k-1:
                if pre_k_last_node:
                    pre_k_last_node.next= first_node_in_current_k
                break
            
            # reverse current k nodes
            head.next= None
            reversed_k= self.reverse_list(first_node_in_current_k)
            
            if pre_k_last_node:
                pre_k_last_node.next= reversed_k
                
            pre_k_last_node= first_node_in_current_k
            
            if not new_head:
                new_head= reversed_k
            
            head= tail
            if tail:
                tail= tail.next
            if not tail:
                pre_k_last_node.next= head
            
        return new_head
        
    
    def reverse_list(self, head):
        pre= None
        tail= None
        
        while head:
            temp= head.next
            head.next= pre
            pre= head
            head= temp
            
        return pre