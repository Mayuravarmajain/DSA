class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch,0) + 1

        for ch in t:
            freq[ch] = freq.get(ch,0) - 1
        ans = 0

        for value in freq.values():
            ans += abs(value)

        return ans