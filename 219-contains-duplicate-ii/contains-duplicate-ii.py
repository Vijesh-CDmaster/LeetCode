class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = {}
        
        for i in range(len(nums)):
            num = nums[i]
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
            
        return False