def pair_target_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

def pair_target_sum_hash(arr, target):
    nums = {}
    for i, num in enumerate(arr):
        nums[num] = i

    for i, num in enumerate(arr):
        if target - num in nums:
            return [nums[target - num], i]
        else:
            nums[arr[i]] = i

pair_target_sum_hash([2,7,11,15], 9)

def two_sum(arr, target):
    nums = {}

    for i, num in enumerate(arr):
        nums[num] = i

    for i, num in enumerate(arr):
        current_sum = target - num
        if current_sum in nums:
            pair = [nums[target - num], i]
            if pair[0] != pair[1]:
                return pair

