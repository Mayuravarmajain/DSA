class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        sort_s = sorted(s)
        sort_t = sorted(t)

        if sort_s == sort_t:
            return True
        else:
            return False