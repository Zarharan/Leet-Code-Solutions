# URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# 19. Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        # Time and space complexity = O(n), run time on leetcode= 88 ms
        def first_solution(head):       
        
            def reverse_list(head):
                new_head= None
                tail= new_head
                while head:
                    tail = head
                    head= head.next
                    tail.next = new_head
                    new_head= tail

                return tail


            reversed_head = reverse_list(head)        
            if n == 1:
                return reverse_list(reversed_head.next)

            counter= 1
            tail= reversed_head
            head= reversed_head
            reversed_head= reversed_head.next           
            while reversed_head:
                counter += 1
                if counter == n:
                    reversed_head= reversed_head.next

                tail.next = reversed_head
                tail = tail.next
                if reversed_head:
                    reversed_head= reversed_head.next

            return reverse_list(head)
        
        
        # Time and space complexity = O(n), run time on leetcode= 62 ms
        def second_solution(head):
            tail= head
            counter = 1
            while counter<= n:
                tail = tail.next
                counter+= 1
            
            if not tail:
                return head.next
            
            target_node_finder = head
            while tail.next:                                
                tail= tail.next
                target_node_finder= target_node_finder.next
                    
            target_node_finder.next= target_node_finder.next.next
            
            return head
            
            
        if not head.next and n == 1:
            return None
        
        # return first_solution(head)
        return second_solution(head)