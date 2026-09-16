from collections import Counter

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counts = Counter(arr)
        return len(counts.values()) == len(set(counts.values()))