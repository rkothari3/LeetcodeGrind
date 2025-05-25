class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Brute force approach
        # - O(n^2) time complexity
        # - O(n) space complexity
        # while '()' in s or '{}' in s or '[]' in s:
        #     s = s.replace('()', '')
        #     s = s.replace('{}', '')
        #     s = s.replace('[]', '')
        # return s == ''

        # Stack
        # - O(n) time & space complexity
        stack = []

        closeToOpenDict = { ")" : "(", "]" : "[", "}" : "{" } # Key=closed, value=open

        for c in s:
            if c in closeToOpenDict: # check if character in string a closing paran.
                if stack and stack[-1] == closeToOpenDict[c]:
                    stack.pop()
                else: # If they don't match or if empty
                    return False
            else: # If the character not a closing para. add it to stack
                stack.append(c)
        return True if not stack else False