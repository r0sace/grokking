def string_anagrams(string, pattern):
    start = 0
    ch_freq = {}
    matches = 0
    result = []

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

        if matches == len(pattern):
            result.append(start)

        if (end-start + 1) > len(pattern) - 1:
            left_ch = string[start]
            start += 1
            if left_ch in ch_freq:
                if ch_freq[left_ch] == 0:
                    matches -= 1
                ch_freq[left_ch] += 1

    return result

string_anagrams('baa', 'aa')




