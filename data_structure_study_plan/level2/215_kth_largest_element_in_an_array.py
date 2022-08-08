# URL: https://leetcode.com/problems/kth-largest-element-in-an-array/

# 215. Kth Largest Element in an Array

# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# You must solve it in O(n) time complexity.

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
 
# Constraints:

# 1 <= k <= nums.length <= 10**5
# -10**4 <= nums[i] <= 10**4


# Solution 1: Using min heap for k items. Time complexity = O(k + (n-k)log(k))
# Runtime: 2177 ms, faster than 9.72% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 27.3 MB, less than 10.44% of Python3 online submissions for Kth Largest Element in an Array.
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        self.min_heap= []
        
        # Create Min heap for the first k elements
        for num in nums[:k]:
            self.heapify_up(num)
        
        # compare other elements with the root of min heap
        for num in nums[k:]:
            
            # if an element is greater than root, make it root and the heapify. At the end, the root is kth largest element.
            if num>self.min_heap[0]:
                self.min_heap[0]= num            
                self.heapify_down()
            
        return self.min_heap[0]
    
        
    def heapify_up(self, num):
        
        self.min_heap.append(num)
                
        child_idx= len(self.min_heap)-1
        while child_idx>= 1:
            parent_idx= (child_idx + 1)//2 - 1
            if self.min_heap[child_idx]< self.min_heap[parent_idx]:
                self.min_heap[child_idx], self.min_heap[parent_idx]= self.min_heap[parent_idx], self.min_heap[child_idx]
            
            child_idx= parent_idx
            
    
    def heapify_down(self):                
        
        index= 0
        while index< len(self.min_heap)//2:
            f_child= (index+1)*2 - 1
            s_child= (index+1)*2            
            
            min_val= self.min_heap[index]
            min_val_idx= index
            if f_child<len(self.min_heap) and self.min_heap[f_child]<self.min_heap[index]:
                min_val= self.min_heap[f_child]
                min_val_idx= f_child
            
            if s_child<len(self.min_heap) and self.min_heap[s_child]<min_val:
                min_val= self.min_heap[s_child]
                min_val_idx= s_child
            
            if min_val_idx == index:
                break
            
            self.min_heap[index], self.min_heap[min_val_idx]= self.min_heap[min_val_idx], self.min_heap[index]
            index= min_val_idx

    
# Solution 2: Using normal max heap. Time complexity = O(nlog(n))
# Runtime: 9012 ms, faster than 5.00% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 27.2 MB, less than 14.18% of Python3 online submissions for Kth Largest Element in an Array.    
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        self.max_heap= []
        
        # create max heap
        for num in nums:
            self.heapify_up(num)
        
        # get largest item k times
        kth_largest= 0
        for idx in range(k):
            kth_largest= self.heapify_down()
            
        return kth_largest
    
        
    def heapify_up(self, num):
        
        self.max_heap.append(num)
                
        child_idx= len(self.max_heap)-1
        while child_idx>= 1:
            parent_idx= (child_idx + 1)//2 - 1
            if self.max_heap[child_idx]> self.max_heap[parent_idx]:
                self.max_heap[child_idx], self.max_heap[parent_idx]= self.max_heap[parent_idx], self.max_heap[child_idx]
            
            child_idx= parent_idx
            
    
    def heapify_down(self):
        
        largest= self.max_heap.pop(0)
        if len(self.max_heap)< 1:
            return largest
        
        last_item = self.max_heap.pop()
        
        self.max_heap.insert(0, last_item)
        
        index= 0
        while index< len(self.max_heap)//2:
            f_child= (index+1)*2 - 1
            s_child= (index+1)*2            
            
            max_val= self.max_heap[index]
            max_val_idx= index
            if f_child<len(self.max_heap) and self.max_heap[f_child]>self.max_heap[index]:
                max_val= self.max_heap[f_child]
                max_val_idx= f_child
            
            if s_child<len(self.max_heap) and self.max_heap[s_child]>max_val:
                max_val= self.max_heap[s_child]
                max_val_idx= s_child
            
            if max_val_idx == index:
                break
            
            self.max_heap[index], self.max_heap[max_val_idx]= self.max_heap[max_val_idx], self.max_heap[index]
            index= max_val_idx
                
        return largest