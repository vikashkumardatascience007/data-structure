def non_repeating_chars(s: str) -> list:
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    return [ch for ch in s if freq[ch] == 1]


print(non_repeating_chars("programming"))
