from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # make set for o(1) look up
        longest = 0

        for n in nums:
            if (n - 1) not in numSet: # If n - 1 not in set, then it start of new seq
                length = 0
                while (n + length) in numSet:
                    # Ex: Suppose n = 2; Case: [2, 20, 4, 10, 3, 4, 5]
                    # n + 0 = 2 Yuh
                    # n + 1 = 3 Yuh
                    # n + 2 = 4 Yuh
                    # n + 3 = 5 Nah - Terminate Loop
                    length += 1
                longest = max(length, longest)
        return longest