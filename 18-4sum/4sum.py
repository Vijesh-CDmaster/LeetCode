class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                l = j + 1
                r = len(nums) - 1

                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]

                    if s == target:
                        x = [nums[i], nums[j], nums[l], nums[r]]
                        if x not in ans:
                            ans.append(x)
                        l += 1
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1

        return ans