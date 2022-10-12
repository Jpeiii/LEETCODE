'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Reference: https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

'''


def maxSubArray(nums):
    max_so_far = max_ending_here = nums[0]

    for i in range(1, len(nums)):
        max_so_far = max(nums[i], max_so_far + nums[i])
        max_ending_here = max(max_ending_here, max_so_far)
    return max_ending_here
