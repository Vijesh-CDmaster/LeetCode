class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        maxi = 0
        seen = set()

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            maxi = max(maxi, right - left + 1)

        return maxi



# class Solution(object):

#     def lengthOfLongestSubstring(self, s):

#         seen = set()

#         for i in range(len(s)):
#             if s.count(s[i]) >= 2:
#                 seen.add(s[i])

#         return len(seen)