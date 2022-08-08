# URL: https://leetcode.com/problems/k-closest-points-to-origin/

# 973. K Closest Points to Origin

# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# Example 1:

# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
# Example 2:

# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 
# Constraints:

# 1 <= k <= points.length <= 10**4
# -10**4 < xi, yi < 10**4


class Solution:
    # Runtime: 1116 ms, faster than 63.09% of Python3 online submissions for K Closest Points to Origin.
    # Memory Usage: 20.6 MB, less than 11.24% of Python3 online submissions for K Closest Points to Origin.
    # Time complexity= O(k + (n-k)log(k))
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # Calculate distance of all points to the origin (0,0)
        self.distance= dict()
        for idx, point in enumerate(points):
            self.distance[idx]= sqrt(point[0]**2 + point[1]**2)
        
        # create max-heap for first k points
        self.max_heap= []
        for item in list(self.distance.items())[:k]:
            self.heapify_up(item)
        
        # compare other points with the root of max-heap. If one point is less than the root, replace with the root and heapify again
        for item in list(self.distance.items())[k:]:
            if item[1] < self.max_heap[0][1]:
                self.max_heap[0]= item
                self.heapify_down()
        
        return [points[point[0]] for point in self.max_heap]
    
    
    def heapify_up(self, item):
        self.max_heap.append(item)
        index= len(self.max_heap) - 1
        
        while index>= 1:
            parent_idx= (index + 1)//2 - 1
            
            if self.max_heap[index][1]>self.max_heap[parent_idx][1]:
                self.max_heap[index],self.max_heap[parent_idx]= self.max_heap[parent_idx], self.max_heap[index]
            else:
                break
            
            index= parent_idx
        
        
    def heapify_down(self):
        index= 0
        while index<len(self.max_heap) // 2:
            f_child= (index + 1)*2 -1
            s_child= (index + 1)*2
            
            max_val= self.max_heap[index][1]
            max_val_idx= index
            
            if self.max_heap[f_child][1]> self.max_heap[index][1]:
                max_val= self.max_heap[f_child][1]
                max_val_idx= f_child
                
            if s_child< len(self.max_heap) and self.max_heap[s_child][1]> max_val:
                max_val_idx= s_child
                
            if max_val_idx== index:
                break
            
            self.max_heap[index],self.max_heap[max_val_idx]= self.max_heap[max_val_idx], self.max_heap[index]
            index= max_val_idx