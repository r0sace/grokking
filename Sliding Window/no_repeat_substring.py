def no_repeat_substring(string):
    start = 0
    characters = {}
    max_substring = 0

    for end in range(len(string)):
        if string[end] not in characters:
            characters[string[end]] = 1
        else:
            characters[string[end]] += 1
            while characters[string[end]] > 1:
                characters[string[start]] -= 1
                start += 1

        max_substring = max(max_substring, end-start+1)


no_repeat_substring('aabccbb')