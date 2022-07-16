# URL: https://leetcode.com/problems/flood-fill/

# 733. Flood Fill

# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.

 

# Example 1:


# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
# Example 2:

# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
# Output: [[0,0,0],[0,0,0]]
# Explanation: The starting pixel is already colored 0, so no changes are made to the image.
 

# Constraints:

# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], color < 2**16
# 0 <= sr < m
# 0 <= sc < n


from collections import defaultdict

class Graph:
    def __init__(self, matrix):
        self.adjacents= defaultdict(list)
        self.unmarked_vertex= set()
        
        adjacents_indexes= [[1,0],[0,1],[-1,0],[0,-1]]        
        for row_idx, row in enumerate(matrix):
            for col_idx, item in enumerate(row):
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
    
    
    def find_flood_indexes_with_bfs(self, start_row, start_col):
        start_key= self.get_key(start_row,start_col)
        target_q= self.get_adjacents(start_key)
        flood_indexes= [start_key]
        
        while target_q:            
            vertex= target_q.pop(0)
            if self.is_mark(vertex):
                continue
            
            flood_indexes.append(vertex)
            self.mark(vertex)
            target_q.extend(self.get_adjacents(vertex))
            
        return flood_indexes
    
        
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:             
        
        if image[sr][sc] == color:
            return image
  
        graph= Graph(image)
        
        flood_indexes= graph.find_flood_indexes_with_bfs(sr,sc)

            
        for row_idx in range(len(image)):
            for col_idx in range(len(image[0])):
                if graph.get_key(row_idx, col_idx) in flood_indexes:
                    image[row_idx][col_idx]= color
        
        return image