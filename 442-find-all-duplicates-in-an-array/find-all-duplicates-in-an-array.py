class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        se = {}
        ma = []
        
        for i in nums:
            if i in se:
                se[i] += 1
            else:
                se[i] = 1
                
        for i in se:
            if se[i] > 1:
                ma.append(i)
                
        return ma