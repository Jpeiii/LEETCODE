class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            hashmap[i] = hashmap.get(i, 0) + 1

        for value in hashmap:
            if hashmap[value] == 1:
                return value


# using xor
# if same value, return 0
# if different value, return the value
'''
0 0 0
0 1 1
1 0 1
1 1 0 
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = i ^ res
        return res
