class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        Time Complexity: O(n)
        Space Complexity: O(n) -> NOTE: Can do O(1) using ASCII (look into later)
        '''
        # To iterate over and add the string to the 
        sList = []
        for letter in s:
            if letter.isalnum():
                letter = letter.lower()
                sList.append(letter)
        strList = "".join(sList)
        print(strList)
        # Using the two pointers approach
        left = 0
        right = len(strList) - 1 # Gives u the last element (aka. the rightmost)
        while left < right:
            if strList[left] != strList[right]:
                return False
            left += 1
            right -= 1
        return True

if __name__ == "__main__":
    solution = Solution()
    test_string = "A man, a plan, a canal: Panama"
    result = solution.isPalindrome(test_string)
    print(f"Input: s = \"{test_string}\"")
    print(f"Output: {result}")
    print("Explanation: \"amanaplanacanalpanama\" is a palindrome.")