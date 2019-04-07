def longest_consecutive_characters(s):
    longest = 0, None
    prev_char = None
    current_sequence = {}
    for char in s:
        if current_sequence.get(char) and char == prev_char:
            current_sequence[char] += 1
            if current_sequence[char] > longest[0]:
                longest = current_sequence[char], char
        else:
            current_sequence[char] = 1
            prev_char = char
    return longest


assert longest_consecutive_characters("AABCDDBBBEEA") == (3, "B")
assert longest_consecutive_characters("AAAAABCDDBBBEEA") == (5, "A")

