class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        def contains(arr, target):
            for num in arr:
                if num == target:
                    return True
            return False

        count1 = 0
        count2 = 0

        for num in nums1:
            if contains(nums2, num):
                count1 += 1

        for num in nums2:
            if contains(nums1, num):
                count2 += 1

        return [count1, count2]