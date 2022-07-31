# URL: https://leetcode.com/problems/reorder-list/

# 143. Reorder List

# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:


# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
 

# Constraints:

# The number of nodes in the list is in the range [1, 5 * 10**4].
# 1 <= Node.val <= 1000


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    # First solution. Time comlexity: O(n) and Space comlexity: O(n)
    # Runtime: 212 ms, faster than 5.08% of Python3 online submissions for Reorder List.
    # Memory Usage: 23.9 MB, less than 95.51% of Python3 online submissions for Reorder List.
    def reorderList155(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        all_nodes= dict()
        new_head= head
        counter= 0
        
        while new_head:
            counter+= 1
            all_nodes[counter]= new_head
            new_head= new_head.next
        
        if counter< 3:
            return
        
        new_head= head
        tail= head.next
        index= counter
        changed_nodes= set()
        
        while index>ceil((counter+1)/2):
            new_head.next= all_nodes[index]
            changed_nodes.add(all_nodes[index])
            new_head= new_head.next
            new_head.next = tail
            
            new_head= tail
            tail= tail.next
            
            index -= 1
        
        if new_head.next in changed_nodes:
            new_head.next= None
            
        if tail.next in changed_nodes:
            tail.next= None
            
            
    # Second solution. Time comlexity: O(n) and Space comlexity: O(1)
    # Runtime: 212 ms, faster than 76.5% of Python3 online submissions for Reorder List.
    # Memory Usage: 23.9 MB, less than 64.16% of Python3 online submissions for Reorder 
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # Get middle node
        slow= head
        fast= head
        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next
            
        mid_node= slow
        
        second_reversed_part= self.reverse_list(mid_node.next)
        
        mid_node.next= None
        
        new_head= head
        tail= head.next
        
        while second_reversed_part:
            new_head.next= second_reversed_part
            second_reversed_part= second_reversed_part.next
            new_head= new_head.next
            new_head.next = tail
            
            new_head= tail
            tail= tail.next
        
    
    def reverse_list(self, head):
        
        pre= None
        while head:
            temp= head.next
            head.next= pre
            pre= head
            head= temp
            
        return pre