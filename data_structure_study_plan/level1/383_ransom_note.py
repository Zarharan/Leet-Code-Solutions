from collections import defaultdict

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        if len(ransomNote) > len(magazine):
            return False
        
        if len(ransomNote) == 1 and len(magazine) == 1 and ransomNote != magazine:
            return False
        
        char_count = defaultdict(int)
        
        for char in magazine:
            char_count[char] +=1
            
        for char in ransomNote:
            char_count[char] -= 1
            if char_count[char] < 0:
                return False
            
        return True
        
        