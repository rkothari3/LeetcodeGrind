class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Brute-force approach
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)): # Can't check the same element twice
                if nums[i] + nums[j] == target:
                    return [i, j]

        # Hashmap Approach
        aHMap = {} # Empty Hashmap (Key=Number, Value=Index)
        for index, value in enumerate(nums):
            # We do target - nums[index] to find the complement
            # Particularly check if its already in the Hashmap
            complement = target - value

            if complement in aHMap: # Checking the keys
                return [aHMap[complement], index]
            # otherwise, store this number and its index
            aHMap[value] = index
                