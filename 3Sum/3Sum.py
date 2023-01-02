class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()  # O(nlogn)
        for i in range(len(nums)):  # O(n)
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:  # O(n)
                s = nums[i] + nums[left] + nums[right]
                if s > 0:
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return result

# time complexity: O(n^2)
