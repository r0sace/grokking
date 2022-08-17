def replacing_ones(nums, k):
    start = 0
    max_ones = 0
    max_length = 0

    for end in range(len(nums)):
        if nums[end] == 1:
            max_ones += 1

        while (end - start + 1) - max_ones > k:
            if nums[start] == 1:
                max_ones -= 1
            start += 1

        max_length = max(max_length, end-start+1)

    return max_length

