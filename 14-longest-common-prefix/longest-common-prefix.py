class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        first = strs[0]
        for i in range(len(first)):
            for words in strs[1:]:
                if i == len(words) or words[i] != first[i]:
                    return first[:i]
        return first