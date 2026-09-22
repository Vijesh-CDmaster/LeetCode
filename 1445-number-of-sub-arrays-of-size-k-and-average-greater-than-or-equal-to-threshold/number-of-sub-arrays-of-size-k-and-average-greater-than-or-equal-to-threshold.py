class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        window = sum(arr[:k])
        count = 0

        for i in range(k, len(arr)):
            if window >= k * threshold:
                count += 1

            window = window - arr[i-k] + arr[i]

        if window >= k * threshold:
            count += 1

        return count
        