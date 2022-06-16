class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        sorted_nums = nums[:]
        
        sorted_nums.sort()
        
        
        head = 0
        tail = len(nums) -1
        
        first_value = 0
        second_value = 0
        
        while head < tail:
            target_sum = sorted_nums[head] + sorted_nums[tail]
            if target_sum == target:
                first_value = sorted_nums[head]
                second_value = sorted_nums[tail]
                break
                
            if target_sum > target:
                tail -= 1
            else:
                head += 1
        result = []
        for idx,item in enumerate(nums):
            if (item == first_value) or (item == second_value):
                result.append(idx)
            if len(result)>= 2:
                break
        
        return result