class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi=0
        node=0
        for i in nums:  
            if i==1:
                node+=1
                maxi=max(maxi,node)

            else:
                node=0
        return maxi
                
        