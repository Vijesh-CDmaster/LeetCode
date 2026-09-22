class Solution(object):
    def maximumSubarraySum(self, nums, k):
        window = 0
        seen = set()
        maxi = 0
        left = 0

        for i in range(len(nums)):

            while nums[i] in seen:
                seen.remove(nums[left])
                window -= nums[left]
                left += 1

            seen.add(nums[i])
            window += nums[i]

            if i - left + 1 == k:
                maxi = max(maxi, window)

                seen.remove(nums[left])
                window -= nums[left]
                left += 1

        return maxi