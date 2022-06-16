from collections import defaultdict

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 0
        
        char_hash= defaultdict(int)
        
        for char in s:
            char_hash[char] += 1
            
        for i in range(len(s)):
            if char_hash[s[i]] == 1:
                return i
        
        return -1
        