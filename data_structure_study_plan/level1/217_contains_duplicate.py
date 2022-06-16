class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        existed = dict()
        result = False
        for i in nums:
            if i in existed:
                result= True
                break
            
            existed[i] = True
        
        return result