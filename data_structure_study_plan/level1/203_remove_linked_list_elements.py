# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        if head == None:
            return None
        
        new_head = None
        result_head = None
        
        while head:
            if head.val != val:
                if result_head == None:
                    result_head = head
                    new_head = result_head
                else:
                    new_head.next = head
                    new_head = new_head.next
            
            head = head.next
        
        if new_head != None:
            new_head.next = None
        
        return result_head