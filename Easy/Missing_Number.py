class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Awful Approach but works
        # aNum = 0

        # for num in range(len(nums) + 1):
        #     if num not in nums:
        #         aNum += num
        #     else:
        #         continue

        # return aNum  


        # Optimized Approach
        '''
        # Length of nums is 3
        # expected sum 1 + 2 + 3 = 6
        # nums = [3,0,1]
        # currentSum = 3 + 0 + 1 = 4
        '''
        n = len(nums)

        # Formula to get the sum of the first n natural numbers.
        expectedSum = n * (n + 1) // 2

        # Current sum
        currentSum = sum(nums)

        return expectedSum - currentSum
