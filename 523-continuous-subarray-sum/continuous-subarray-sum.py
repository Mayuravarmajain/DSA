class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prefix = 0 
        remin_ind ={0:-1}

        for i in range(len(nums)):

            prefix += nums[i]

            remainder = prefix % k

            if remainder in remin_ind:

                if i - remin_ind[remainder] >=2:
                    return True
            else:
                remin_ind[remainder] =  i

        return False