def smallest_window_substring(string, pattern):
    start = 0
    matches = 0
    ch_freq = {}
    substring = 0
    min_length = len(string) + 1

    for ch in pattern:
        if ch not in ch_freq:
            ch_freq[ch] = 0
        ch_freq[ch] += 1

    for end in range(len(string)):
        right_ch = string[end]

        if right_ch in ch_freq:
            ch_freq[right_ch] -= 1
            if ch_freq[right_ch] == 0:
                matches += 1

        while matches == len(pattern):
            if min_length > end - start + 1:
                min_length = end - start + 1
                substring = start



