# URL: https://leetcode.com/problems/rotting-oranges/

# 994. Rotting Oranges

# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# Example 1:

# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 
# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.


from collections import defaultdict

class Graph:
    def __init__(self, matrix):
        self.adjacents= defaultdict(list)
        self.unmarked_vertex= set()
        self.vertexs= defaultdict(int)
        self.rottens= []
        
        adjacents_indexes= [[1,0],[0,1],[-1,0],[0,-1]]        
        for row_idx in range(len(matrix)):
            for col_idx in range(len(matrix[0])):
                vertex_key= self.get_key(row_idx, col_idx)                
                self.vertexs[vertex_key]= matrix[row_idx][col_idx]
                
                if matrix[row_idx][col_idx] == 0:
                    continue
                
                if matrix[row_idx][col_idx] == 2:
                    self.rottens.append(vertex_key)                    
                
                self.unmarked_vertex.add(vertex_key)
                for adj in adjacents_indexes:
                    if row_idx+adj[0] >= 0 and row_idx+adj[0]< len(matrix) and col_idx+adj[1] >= 0 and col_idx+adj[1]< len(matrix[0]) and matrix[row_idx+adj[0]][col_idx+adj[1]] in [1,2]:                       
                        
                        self.adjacents[vertex_key].append(self.get_key(row_idx+adj[0], col_idx+adj[1]))
                    

    def get_key(self, row_idx, col_idx):
        return str(row_idx)+"#"+str(col_idx)

    
    def get_value(self, vertex_key):
        return self.vertexs[vertex_key]
    
    
    def set_value(self, vertex_key, value):
        self.vertexs[vertex_key]= value
    
    
    def get_adjacents(self, vertex):
        return self.adjacents[vertex]
    
    
    def mark(self, vertex):
        if vertex in self.unmarked_vertex:
            self.unmarked_vertex.remove(vertex)
            
    
    def is_mark(self, vertex):
        return not vertex in self.unmarked_vertex
    
    
    def get_unmarked(self):
        if len(self.unmarked_vertex)>0:
            target_vertex= self.unmarked_vertex.pop()
            self.unmarked_vertex.add(target_vertex)
            return target_vertex
        
        return None
    
    
    def calc_min_minute_using_bfs(self):
        
        bfs_q=[]
        final_time= 0
        for rotten_o in self.rottens:
            bfs_q.append((rotten_o, 0))
        
        # BFS
        while bfs_q:
            target_v, time= bfs_q.pop(0)
            final_time= max(final_time,time)
            
            if self.is_mark(target_v):
                continue

            self.mark(target_v)
            
            adjacents= self.get_adjacents(target_v)
            for adj in adjacents:
                if self.get_value(adj)== 1:
                    bfs_q.append((adj, time+1))
                    self.set_value(adj, 2)
                        
        if self.get_unmarked():
            return -1
        
        return final_time
    

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        graph= Graph(grid)
        
        return graph.calc_min_minute_using_bfs()