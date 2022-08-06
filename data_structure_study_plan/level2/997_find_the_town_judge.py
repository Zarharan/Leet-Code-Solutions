# URL: https://leetcode.com/problems/find-the-town-judge/

# 997. Find the Town Judge

# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise. 

# Example 1:

# Input: n = 2, trust = [[1,2]]
# Output: 2
# Example 2:

# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3
# Example 3:

# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
 
# Constraints:

# 1 <= n <= 1000
# 0 <= trust.length <= 10**4
# trust[i].length == 2
# All the pairs of trust are unique.
# ai != bi
# 1 <= ai, bi <= n


from collections import defaultdict
class Solution:
    
    # Runtime: 998 ms, faster than 67.83% of Python3 online submissions for Find the Town Judge.
    # Memory Usage: 19 MB, less than 28.54% of Python3 online submissions for Find the Town Judge.
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        if n == 1:
            return 1
        
        judge_counter= defaultdict(int)
        trust_people= defaultdict(int)
        candidates= []
        for item in trust:
            judge_counter[item[1]] += 1
            trust_people[item[0]]+= 1
            
            if judge_counter[item[1]] == n-1:
                candidates.append(item[1])
                
        if len(candidates)<1:
            return -1
        
        for candidate in candidates:
            if trust_people[candidate] == 0:
                return candidate
            
        return -1