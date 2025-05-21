class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hMap = {} # key = same sorted letters, value = list of strings that can be build from those sorted letters, these strings are anagrams of each other.
        for s in strs:
            # Need to convert sorted result to tuple since lists can't be dict keys
            sorted_s = tuple(sorted(s))
            if sorted_s not in hMap:
                hMap[sorted_s] = [s]
            else:
                hMap[sorted_s].append(s)
        return list(hMap.values())


if __name__ == "__main__":
    solution = Solution()
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    result = solution.groupAnagrams(strs)
    print(f"Input: strs = {strs}")
    print(f"Output: {result}")