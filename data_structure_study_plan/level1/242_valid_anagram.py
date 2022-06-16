from collections import defaultdict

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        char_count = defaultdict(int)        
        
        for char in s:
            char_count[char] += 1
            
        for char in t:
            char_count[char] -= 1
            
            if char_count[char]<0:
                return False
            
        return True