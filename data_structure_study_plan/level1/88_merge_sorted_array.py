class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        head = m -1
        tail = len(nums1) - 1
        tail2 = n - 1
        while tail2 >= 0:            
            if nums2[tail2] >= nums1[head] or head <0:
                nums1[tail] = nums2[tail2]                
                tail2 -= 1
            else:
                nums1[tail] = nums1[head]
                head -= 1
                
            tail -= 1
                