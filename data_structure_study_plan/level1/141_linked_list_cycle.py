from collections import defaultdict

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head == None:
            return False
        
        node_counter = defaultdict(int)
        
        while head.next != None:
                        
            node_counter[id(head)] += 1
            if node_counter[id(head)] > 1:
                return True
            
            head = head.next
        
        return False