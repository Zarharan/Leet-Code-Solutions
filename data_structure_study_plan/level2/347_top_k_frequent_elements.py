# URL: https://leetcode.com/problems/top-k-frequent-elements/

# 347. Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 
# Constraints:

# 1 <= nums.length <= 10**5
# -10**4 <= nums[i] <= 10**4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


from collections import defaultdict
class Solution:
    
    # Runtime: 115 ms, faster than 87.59% of Python3 online submissions for Top K Frequent Elements.
    # Memory Usage: 18.8 MB, less than 47.75% of Python3 online submissions for Top K Frequent Elements.
    # Time complexity= O(max(k,n) + (n-k)log(k))
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # count frequency of each number
        counter_dict= defaultdict(int)
        for num in nums:
            counter_dict[num]+= 1
        
        # create min-heap for k first items
        self.min_heap= []
        for item in list(counter_dict.items())[:k]:
            self.heapify_up(item[0], item[1])
        
        # compare other elements with the root of min-heap
        for item in list(counter_dict.items())[k:]:
            # if frequency of an element is greater than root, make it root and then heapify. At the end, the min-heap is top k frequent elements.
            if item[1]>self.min_heap[0][1]:
                self.min_heap[0] = (item[0], item[1])
                self.heapify_down()
        
        return [x[0] for x in self.min_heap]
    
    
    def heapify_up(self, key, val):
        
        self.min_heap.append((key, val))
                
        child_idx= len(self.min_heap)-1
        while child_idx>= 1:
            parent_idx= (child_idx + 1)//2 - 1
            if self.min_heap[child_idx][1]< self.min_heap[parent_idx][1]:
                self.min_heap[child_idx], self.min_heap[parent_idx]= self.min_heap[parent_idx], self.min_heap[child_idx]
            
            child_idx= parent_idx
            
    
    def heapify_down(self):                
        
        index= 0
        while index< len(self.min_heap)//2:
            f_child= (index+1)*2 - 1
            s_child= (index+1)*2            
            
            min_val= self.min_heap[index][1]
            min_val_idx= index
            if f_child<len(self.min_heap) and self.min_heap[f_child][1]<self.min_heap[index][1]:
                min_val= self.min_heap[f_child][1]
                min_val_idx= f_child
            
            if s_child<len(self.min_heap) and self.min_heap[s_child][1]<min_val:
                min_val= self.min_heap[s_child][1]
                min_val_idx= s_child
            
            if min_val_idx == index:
                break
            
            self.min_heap[index], self.min_heap[min_val_idx]= self.min_heap[min_val_idx], self.min_heap[index]
            index= min_val_idx