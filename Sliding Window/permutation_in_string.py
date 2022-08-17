def permutations_in_string(string, pattern):
    start = 0
    matches = 0
    pattern_freq = {}

    for ch in pattern:
        if ch not in pattern_freq:
            pattern_freq[ch] = 0
        pattern_freq[ch] += 1

    for end in range(len(string)):
        right_ch = string[end]
        if right_ch in pattern_freq:
            pattern_freq[right_ch] -= 1
            if pattern_freq[right_ch] == 0:
                matches += 1

        if matches == len(pattern_freq):
            return True

        if (end - start + 1) > len(pattern)-1:
            left_ch = string[start]
            start += 1
            if left_ch in pattern_freq:
                if pattern_freq[left_ch] == 0:
                    matches -= 1
                pattern_freq[left_ch] += 1

    return False

permutations_in_string("eidboaoo", "ab")
