def rotate(nums, k):
    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    '''
    Perform k%N in order to keep the value of d within the range of the array where 
    k is the number of times the array is rotated and N is the size of the array.
    '''
    k = k % len(nums)
    left = 0
    right = len(nums)-1
    nums.reverse()
    reverse(nums, 0, k-1)
    reverse(nums, k, right)
    return nums


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
result = rotate(nums, k)
print(result)
