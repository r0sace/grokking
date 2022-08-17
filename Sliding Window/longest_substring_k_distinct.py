# Given a string, find the length of the longest substring in it with no more
# than k distinct characters. You can assume K is less than or equal to the
# length of the given string.
#
# Example:
#           Input: String = "araaci", k = 2
#           Output: 4
#           The longest substring with no more than '2' distinct characters is "araa"

def longest_substring_k_distinct(str, k):
    start = 0
    character_count = {}
    max_length = 0

    for end in range(len(str)):
        if str[end] not in character_count:
            character_count[str[end]] = 1
        elif str[end] in character_count:
            character_count[str[end]] += 1

        while len(character_count) > k:
            character_count[str[start]] -= 1
            if character_count[str[start]] == 0:
                del character_count[str[start]]
            start += 1

        max_length = max(max_length, end-start + 1)

    return max_length


