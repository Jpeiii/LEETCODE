class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def hash(nums):
            hashmap = {}
            for n in nums:
                if n not in hashmap:
                    hashmap[n] = 0
                hashmap[n] = hashmap.get(n, 0) + 1
            return hashmap

        h1 = hash(nums1)
        h2 = hash(nums2)
        result = []
        for i in h1:
            if i in h2:
                frequent = min(h1[i], h2[i])
                for j in range(frequent):
                    result.append(i)
        return result
