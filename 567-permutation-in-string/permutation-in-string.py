from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        target = Counter(s1)
        window = Counter(s2[:len(s1)])

        if target == window:
            return True

        for i in  range(len(s1),len(s2)):
            window[s2[i]] +=1

            left_char = s2[i- len(s1)]
            window[left_char] -= 1

            if window[left_char] == 0:
                del window[left_char]

            if window == target:
                return True

        return False
