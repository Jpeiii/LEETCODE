class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        frequency = [[] for i in range(len(nums)+1)]
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)

        for key, value in hashmap.items():
            frequency[value].append(key)

        result = []
        for i in range(len(nums), 0, -1):
            for n in frequency[i]:
                result.append(n)
                if (len(result) == k):
                    return result
