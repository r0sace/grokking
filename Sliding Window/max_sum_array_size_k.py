# Given an array of positive numbers and a positive number 'k', find the maximum
# sum of any contiguous subarray of size 'k'.
#
# Example:
#           Input: [2, 1, 5, 1, 3, 2], k = 3
#           Output: 9
#           Subarray with maximum sum = [5, 1, 3]

def max_sub_array_of_size_k(k, arr):
    start = 0
    sum = 0
    max = 0

    for end in range(len(arr)):
        sum += arr[end]

        if end >= k:
            sum -= arr[start]
            start += 1

        if sum > max:
            max = sum

    return max


max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])
