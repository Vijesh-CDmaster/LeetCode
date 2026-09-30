class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        seen={}
        for i in strs:
            b="".join(sorted(i))
            if b in seen:
                seen[b].append(i)
            else:
                seen[b]=[i]
        return seen.values()