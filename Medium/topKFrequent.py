class Solution(object):
    def topKFrequent(self, nums, k):
        # """
        # :type nums: List[int]
        # :type k: int
        # :rtype: List[int]
        # """
        # ### Brute Force Approach - O(nlogn)
        # # HashMap: key = number, value = frequency
        # aDict = {}
        # for num in nums:
        #     if num not in aDict:
        #         aDict[num] = 1
        #     else:
        #         aDict[num] += 1
        # '''
        # {1:1, 2:2, 3:3}, k = 2
        # '''
        # '''
        # How to implement the k part:
        # - Get the length of list (k)
        # '''
        # # aList = list(aDict.values()) # [1, 2, 3] <- Only values
        # items = list(aDict.items()) # [(1,1), (2, 2), (3,3)] <- Key,value pairs
        # #sort the second element in each pair <= Descending
        # items.sort(key=lambda x: x[1], reverse=True) 
        # count = 0
        # result = []
        # for pair in items:
        #     if count == k:
        #         break
        #     else:
        #         count += 1
        #         result.append(pair[0])
        # return result
        
        # Optimized approach - using Bucket Sort
        # Frquency Map - O(n)
        from collections import defaultdict

        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        # Bucket sort - O(n)
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            bucket[freq].append(num)
        '''
        To visualize
        bucket = [
        [],          # index 0 -> no number appears 0 times
        [3],         # index 1 -> number 3 appears once
        [2],         # index 2 -> number 2 appears twice
        [1],         # index 3 -> number 1 appears three times
        [], [], ...  # rest are empty
        ]
        '''
        # Collect Top K freq. elements - O(n)
        result = []
        # range(start, stop, step)
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result

