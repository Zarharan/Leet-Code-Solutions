# URL: https://leetcode.com/problems/permutation-in-string/

# 567. Permutation in String

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 
# Constraints:

# 1 <= s1.length, s2.length <= 10**4
# s1 and s2 consist of lowercase English letters.


from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_dict= defaultdict(int)
        s2_window= defaultdict(int)
        for char in s1:
            s1_dict[char] += 1
            
        for char in s2[:len(s1)]:
            s2_window[char] += 1
        
        if s1_dict == s2_window:
            return True
        
        for index in range(len(s1),len(s2)):
            cur_char= s2[index]
            head_char= s2[index - len(s1)]
            s2_window[head_char] -= 1
            if s2_window[head_char] == 0:
                s2_window.pop(head_char)

            s2_window[cur_char] += 1
            
            if s1_dict == s2_window:
                return True
            
        return False