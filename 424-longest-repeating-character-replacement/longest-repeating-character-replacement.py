class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        count = {}
        maxfreq = 0
        ans = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0) + 1
            maxfreq = max(maxfreq,count[s[right]])

            while (right - left +1) -maxfreq > k:
                count[s[left]] -= 1
                left +=1
            ans = max(ans,right-left +1)

        return ans