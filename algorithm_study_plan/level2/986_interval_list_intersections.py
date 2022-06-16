# Url: https://leetcode.com/problems/interval-list-intersections/

# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.

# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

# The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

 

# Example 1:


# Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# Example 2:

# Input: firstList = [[1,3],[5,9]], secondList = []
# Output: []
 

# Constraints:

# 0 <= firstList.length, secondList.length <= 1000
# firstList.length + secondList.length >= 1
# 0 <= starti < endi <= 10**9
# endi < starti+1
# 0 <= startj < endj <= 10**9
# endj < startj+1


class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(firstList) == 0 or len(secondList)==0:
            return []
        
        
        f_head = 0
        s_head = 0
        result = []
        while f_head < len(firstList) and s_head < len(secondList):
            f_start =firstList[f_head][0]
            f_end = firstList[f_head][1]
            s_start =secondList[s_head][0]
            s_end = secondList[s_head][1]
            
            if f_start < s_start and f_end < s_start:
                f_head +=1
                continue
            
            if f_start > s_start and f_start > s_end:
                s_head +=1
                continue
                
            if f_start >= s_start and f_end <= s_end:
                result.append([f_start, f_end])
                f_head +=1
            elif f_start >= s_start and f_end > s_end:
                result.append([f_start, s_end])
                s_head+=1
            elif s_start>= f_start and s_end <= f_end:
                result.append([s_start, s_end])
                s_head+=1
            elif s_start>= f_start and s_end > f_end:
                result.append([s_start, f_end])
                f_head +=1
            
        return result
                
            
            
            
                
            