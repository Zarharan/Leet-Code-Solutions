# URL: https://leetcode.com/problems/merge-intervals/

# 56. Merge Intervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

# Constraints:

# 1 <= intervals.length <= 10**4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10**4


from collections import defaultdict
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        end_times= defaultdict(int)
        start_times= []
        for item in intervals:
            start_times.append(item[0])
            end_times[item[0]]= max(end_times[item[0]], item[1])
            
        
        start_times.sort()
        
        head= 0
        result= []
        while head< len(start_times):
            start_time= start_times[head]
            end_time= end_times[start_times[head]]
            head+= 1
            while head<len(start_times) and end_time>= start_times[head]:                
                end_time= max(end_times[start_times[head]], end_time)
                head+=1
                
            result.append([start_time, end_time])
            
            
            
        return result