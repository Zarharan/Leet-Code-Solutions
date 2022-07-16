# URL: https://leetcode.com/problems/max-area-of-island/

# 695. Max Area of Island

# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

 

# Example 1:


# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.


from collections import defaultdict

class Graph:
    def __init__(self, matrix):
        self.adjacents= defaultdict(list)
        self.unmarked_vertex= set()
        
        adjacents_indexes= [[1,0],[0,1],[-1,0],[0,-1]]        
        for row_idx, row in enumerate(matrix):
            for col_idx, item in enumerate(row):
                if item == 0:
                    continue
                    
                self.unmarked_vertex.add(self.get_key(row_idx, col_idx))
                for adj in adjacents_indexes:
                    if row_idx+adj[0] >= 0 and row_idx+adj[0]< len(matrix) and col_idx+adj[1] >= 0 and col_idx+adj[1]< len(matrix[0]) and item == matrix[row_idx+adj[0]][col_idx+adj[1]]:
                        self.adjacents[self.get_key(row_idx, col_idx)].append(self.get_key(row_idx+adj[0], col_idx+adj[1])) 
                    

    def get_key(self, row_idx, col_idx):
        return str(row_idx)+"#"+str(col_idx)
    
    
    def get_adjacents(self, vertex):
        return self.adjacents[vertex]
    
    
    def mark(self, vertex):
        if vertex in self.unmarked_vertex:
            self.unmarked_vertex.remove(vertex)
            
    
    def is_mark(self, vertex):
        return not vertex in self.unmarked_vertex
    
    
    def get_unmarked(self):
        if len(self.unmarked_vertex)>0:
            return self.unmarked_vertex.pop()
        
        return None
    

    def cal_area_with_bfs(self, start_vertex):
        target_q= self.get_adjacents(start_vertex)
        area= 1
        
        while target_q:            
            vertex= target_q.pop(0)
            if self.is_mark(vertex):
                continue
                
            area+= 1
            self.mark(vertex)
            target_q.extend(self.get_adjacents(vertex))
        return area
    
    
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        graph= Graph(grid)
        
        unmark_vertex= graph.get_unmarked()
        max_area= 0
        
        while unmark_vertex:
            max_area= max(max_area, graph.cal_area_with_bfs(unmark_vertex))
            unmark_vertex= graph.get_unmarked()
            
        
        return max_area
        
