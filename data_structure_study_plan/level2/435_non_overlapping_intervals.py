# URL: https://leetcode.com/problems/non-overlapping-intervals/

# 435. Non-overlapping Intervals

# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

# Example 1:

# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
# Example 2:

# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
# Example 3:

# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

# Constraints:

# 1 <= intervals.length <= 10**5
# intervals[i].length == 2
# -5 * 10**4 <= starti < endi <= 5 * 10**4


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        
        start_times= defaultdict(list)
        end_times= []
        for item in intervals:
            start_times[item[1]].append(item[0])
            
        
        end_times= sorted(start_times.keys())
        
        counter= 0
        last_item_end_time= float("-inf")
        
        for end in end_times:
            if last_item_end_time> max(start_times[end]):
                counter+= len(start_times[end])
            else:
                last_item_end_time= end
                counter+= len(start_times[end]) -1            
            
        return counter