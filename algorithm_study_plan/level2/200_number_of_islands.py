# URL: https://leetcode.com/problems/number-of-islands/

# 200. Number of Islands

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 
# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.


from collections import defaultdict
class Graph:
    def __init__(self, grid: List[List[str]]):
        self.vertexes = defaultdict(int)
        self.adjacents = defaultdict(list)        
        self.unvisited = set()
        
        for row_idx, row in enumerate(grid):
            for col_idx, item in enumerate(row):
                node_key = "r"+str(row_idx)+"c"+str(col_idx)
                self.vertexes[node_key] = int(item)
                if int(item) == 1:
                    self.unvisited.add(node_key)
                if row_idx -1 >= 0:
                    self.adjacents[node_key].append("r"+str(row_idx-1)+"c"+str(col_idx))
                if row_idx +1 < len(grid):
                    self.adjacents[node_key].append("r"+str(row_idx+1)+"c"+str(col_idx))
                if col_idx -1 >= 0:
                    self.adjacents[node_key].append("r"+str(row_idx)+"c"+str(col_idx-1))
                if col_idx +1 < len(row):
                    self.adjacents[node_key].append("r"+str(row_idx)+"c"+str(col_idx+1))
            
    
    def get_adjacents(self, node_key):
        return self.adjacents[node_key]
    
    
    def get_val(self, node_key):
        return self.vertexes[node_key]
    
    
    def set_visited(self, node_key):
        if node_key in self.unvisited:
            self.unvisited.remove(node_key)
        
    
    def get_visited(self, node_key):
        return (not node_key in self.unvisited)

    
    def get_unvisited(self):
        """
        This function marks an unvisited vertex and returns it.
        """
        
        if len(self.unvisited)>0:
            return self.unvisited.pop()           
        return None
    
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        island_num = 0
        
        graph = Graph(grid)
        unvisited_vertex = graph.get_unvisited()
        
        while unvisited_vertex:
            if graph.get_val(unvisited_vertex) == 1:
                island_num += 1
                self.dfs(unvisited_vertex, graph)
            unvisited_vertex = graph.get_unvisited()
        
        return island_num
        
        
    def dfs(self, vertex, graph):        
        graph.set_visited(vertex)
        adjacents = graph.get_adjacents(vertex)        
        
        for v in adjacents:
            if not graph.get_visited(v) and graph.get_val(v) == 1:
                self.dfs(v, graph)
        