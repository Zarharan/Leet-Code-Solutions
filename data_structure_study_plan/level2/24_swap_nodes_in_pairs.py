# URL: https://leetcode.com/problems/swap-nodes-in-pairs/

# 24. Swap Nodes in Pairs

# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Example 1:

# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Example 2:

# Input: head = []
# Output: []
# Example 3:

# Input: head = [1]
# Output: [1]
 
# Constraints:

# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head== None or head.next== None:
            return head
        
        new_head= None
        first_pointer= head
        second_pointer= head.next
        head= None
        
        while first_pointer and second_pointer:                
            first_pointer.next, second_pointer.next= second_pointer.next, first_pointer

            first_pointer, second_pointer= second_pointer, first_pointer
            
            if new_head == None:
                new_head =first_pointer                
            else:
                head.next = first_pointer
            
            head= second_pointer
            
            if first_pointer.next and second_pointer.next:
                first_pointer= first_pointer.next.next
                second_pointer= second_pointer.next.next
            else:
                break
        
        return new_head