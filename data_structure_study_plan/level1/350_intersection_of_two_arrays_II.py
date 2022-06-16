from collections import defaultdict

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """       
        
        if len(nums1) > len(nums2):
            self.create_dict(nums2)
            return self.find_intersection(nums1)
        else:
            self.create_dict(nums1)
            return self.find_intersection(nums2)
            
    
    def find_intersection(self, nums):
        result = []
        for item in nums:
            if self.my_dict[item] > 0:
                self.my_dict[item] -= 1
                result.append(item)
        return result
                
        
    
    def create_dict(self, nums):
        self.my_dict = defaultdict(int)
        for item in nums:
            self.my_dict[item] += 1