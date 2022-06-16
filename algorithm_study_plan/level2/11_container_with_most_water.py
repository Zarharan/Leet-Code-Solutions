# Url: https://leetcode.com/problems/container-with-most-water/

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:

# n == height.length
# 2 <= n <= 10**5
# 0 <= height[i] <= 10**4


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        return self.optimum(height)

        
    def optimum(self, height):
        
        head = 0
        tail = len(height)-1
        most_water = 0
        
        while head<tail:
            current_min = min(height[head], height[tail])
            water_amount = current_min * (tail-head)
            if water_amount>most_water:
                most_water = water_amount           
            if height[head]< height[tail]:
                head +=1
            else:
                tail -=1
            
        return most_water
    
    
    def brute_force(self, height):
        most_water = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                current_min = min(height[j], height[i])
                water_amount = current_min * ((j+1)-(i+1))
                if water_amount>most_water:
                    most_water = water_amount
                  
        return most_water