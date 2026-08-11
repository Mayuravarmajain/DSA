class Solution(object):
    def threeSum(self, nums):

        nums.sort()
        result = []

        for n in range(len(nums) - 2):

            if n > 0 and nums[n] == nums[n-1]:
                continue

            left = n + 1
            right = len(nums) - 1

            while left < right:

                total = nums[n] + nums[left] + nums[right]

                if total == 0:

                    result.append([nums[n], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1

                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return result