# URL: https://leetcode.com/problems/shortest-path-in-binary-matrix/

# 1091. Shortest Path in Binary Matrix

# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

 

# Example 1:


# Input: grid = [[0,1],[1,0]]
# Output: 2
# Example 2:


# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
# Example 3:

# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
 

# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1

from collections import defaultdict

class Graph:
    def __init__(self, matrix):
        self.vertexs = dict()
        self.adjacents = defaultdict(list)
        self.unvisited = set()
        self.previous_node = dict()
        neighbor_idx = [[-1,0], [1,0], [0,-1], [0,1], [1,1],[-1,1],[1,-1],[-1,-1]]
        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                hash_key= self.get_vertex_hash_key(i,j)
                self.vertexs[hash_key] = matrix[i][j]
                if matrix[i][j]==0:
                    self.unvisited.add(hash_key)
                    
                    for n_idx in neighbor_idx:
                        if i+n_idx[0]<len(matrix) and i+n_idx[0]>=0 and j+n_idx[1]<len(matrix[0]) and j+n_idx[1]>=0 and matrix[i+n_idx[0]][j+n_idx[1]] == 0:
                            self.adjacents[hash_key].append(self.get_vertex_hash_key(i+n_idx[0],j+n_idx[1]))
        
                
    def get_vertex_hash_key(self, i,j):
        return "r" + str(i) + "c" + str(j)
        
        
    def get_vertex(self, i,j):
        return self.vertexs[self.get_vertex_hash_key(i,j)]
    
    def get_adjacents(self, vertex):
        return self.adjacents[vertex]
    
    
    def mark(self, vertex):
        if vertex in self.unvisited:
            self.unvisited.remove(vertex)
            
            
    def is_mark(self, vertex):
        return not vertex in self.unvisited
        
        
    def get_unvisited_vertex(self):
        if len(self.unvisited)>0:
            return self.unvisited.pop()
        
        return None
    
    
    def set_previous_vertex(self,vertex, prev_vertex):
        if vertex not in self.previous_node:
            self.previous_node[vertex] = prev_vertex
            
    
    def get_previous_vertex(self, vertex):
        if vertex in self.previous_node:
            return self.previous_node[vertex]
        return None
    

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] !=0 or grid[len(grid)-1][len(grid)-1] !=0:
            return -1
        
        if len(grid[0]) == 1:
            if grid[0][0] !=0:
                return -1
            return 1
        
        graph = Graph(grid)
        distination_key = graph.get_vertex_hash_key(len(grid)-1,len(grid)-1)
        start_vertext= graph.get_vertex_hash_key(0,0)
        bfs_q = [start_vertext]
        graph.set_previous_vertex(start_vertext, None)

        while len(bfs_q)>0:
            vertex= bfs_q.pop(0)
            if graph.is_mark(vertex):
                continue
            graph.mark(vertex)            
            adjacents= graph.get_adjacents(vertex)
            for v in adjacents:
                graph.set_previous_vertex(v, vertex)
            bfs_q.extend(adjacents)
            
            if distination_key == vertex:
                break
            
        prev_vertex= graph.get_previous_vertex(distination_key)
            
        if not prev_vertex:
            return -1
        
        path_length = 1
        
        while prev_vertex:
            path_length += 1
            prev_vertex= graph.get_previous_vertex(prev_vertex)
        
        return path_length
            
