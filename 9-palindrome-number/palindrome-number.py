class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        reverse_number = 0
        temp = x
        while temp !=0:
            digit = temp % 10
            reverse_number = reverse_number*10 + digit
            temp //= 10
        return reverse_number == x

            