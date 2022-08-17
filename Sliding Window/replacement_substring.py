def replacement_substring(string, k):
    start = 0
    character_count = {}
    max_repeating = 0
    max_length = 0

    for end in range(len(string)):
        if string[end] not in character_count:
            character_count[string[end]] = 1
        else:
            character_count[string[end]] += 1

        max_repeating = max(max_repeating, character_count[string[end]])

        if (end - start + 1) - max_repeating > k:
            character_count[string[start]] -= 1
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length

replacement_substring('abbcb', 1)