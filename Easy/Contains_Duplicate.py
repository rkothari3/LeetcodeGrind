class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True  # Found a duplicate
            seen.add(num)
        return False  # No duplicates found

        # Hella-optimal approach
        if len(set(nums)) != len(nums):
            return True
        else:
            return False