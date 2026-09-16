from collections import Counter


class Solution(object):

  def sumOfUnique(self, nums):
    """:type nums: List[int]

    :rtype: int
    """
    counts = Counter(nums)
    return sum(num for num, count in counts.items() if count == 1)