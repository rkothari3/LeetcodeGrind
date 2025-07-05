from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftPointer = 0
        rightPointer = len(heights) - 1

        maxArea = 0

        while leftPointer < rightPointer:
            # To find area
            width = rightPointer - leftPointer
            height = min(heights[leftPointer], heights[rightPointer])

            Area = width * height
            # print(Area)
            if Area > maxArea:
                maxArea = Area

            if heights[leftPointer] < heights[rightPointer]:
                leftPointer += 1
            else:
                rightPointer -= 1
        return maxArea


if __name__ == "__main__":
    # Example usage
    heights = [1,7,2,5,4,7,3,6]
    sol = Solution()
    result = sol.maxArea(heights)
    print("Max area:", result)
