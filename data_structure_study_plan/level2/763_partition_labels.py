# URL: https://leetcode.com/problems/partition-labels/

# 763. Partition Labels

# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

# Example 1:

# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
# Example 2:

# Input: s = "eccbbbbdec"
# Output: [10] 

# Constraints:

# 1 <= s.length <= 500
# s consists of lowercase English letters.


from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_pos= defaultdict(int)
        
        for idx, char in enumerate(s):
            last_pos[char]= idx
            
        index= 0
        result= [0]
        next_break= -1
        last_break_index= -1
        while index< len(s):
            target_char= s[index]
            next_break= max(next_break, last_pos[target_char])
            if index==next_break:                
                result.append(index - last_break_index)
                last_break_index= index
            
            index+= 1
            
        result.pop(0)
        return result