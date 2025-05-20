class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # First, check if they're both the same length
        if len(s) != len(t):
            return False

        aDict = {}  # key = letter, value = count
        bDict = {}

        for letter in s:
            if letter in aDict:
                aDict[letter] += 1
            else:
                aDict[letter] = 1

        for letter in t:
            if letter in bDict:
                bDict[letter] += 1
            else:
                bDict[letter] = 1

        print(aDict)
        print(bDict)
        
        return aDict == bDict

if __name__ == "__main__":
    sol = Solution()
    s = "racecar"
    t = "carrace"
    print("Example 1:")
    print("Input: s =", s, ", t =", t)
    print("Output:", sol.isAnagram(s, t))