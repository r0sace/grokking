def first_unique_brute(s):
    flag = False
    letter_set = set()

    for i, ch in enumerate(s):
        if ch in letter_set:
            continue
        for j in range(i + 1, len(s)):
            if ch == s[j]:
                flag = True
        if flag is False:
            return i
        flag = False
        letter_set.add(ch)

    return -1
