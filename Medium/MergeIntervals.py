class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # sort the array by the first element in the sub array
        intervals.sort(key=lambda x: x[0])

        # Create a new list which will be returned with the merged intervals
        # Begin with the first interval already in it
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            last_merged = merged[-1]
            current_interval = intervals[i]

            if last_merged[1] >= current_interval[0]:
                last_merged[1] = max(last_merged[1], current_interval[1])
            else:
                merged.append(current_interval)
        return merged

# Example usage:
solution = Solution()
print(solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # Output: [[1, 6], [8, 10], [15, 18]]
print(solution.merge([[1, 4], [4, 5]]))  # Output: [[1, 5]]
print(solution.merge([[1, 4], [2, 3]]))  # Output: [[1, 4]]