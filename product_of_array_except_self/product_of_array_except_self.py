'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

'''

# time complexity: O(n) as the array only iterate n times


def productExceptSelf(nums):
    n = len(nums)
    prefix, postfix = 1, 1
    res = [1] * n

    # get the product of nums[i] from left to right, not include the last element
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    # res = [1,1,2,6]

    # get the product of nums[i] from right to left (ascending the index), not include the first element
    for i in range(n-1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res
