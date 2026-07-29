from collections import Counter
class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        count = Counter(s)
        for ch in t:
            if count[ch] > 0:
                count[ch] -= 1
        return sum(count.values())
