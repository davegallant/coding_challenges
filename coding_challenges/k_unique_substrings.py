"""
"aabbcc", k = 1
Max substring can be any one from {"aa" , "bb" , "cc"}.

"aabbcc", k = 2
Max substring can be any one from {"aabb" , "bbcc"}.

"aabbcc", k = 3
There are substrings with exactly 3 unique characters
{"aabbcc" , "abbcc" , "aabbc" , "abbc" }
Max is "aabbcc" with length 6.

"aaabbb", k = 3
There are only two unique characters, thus show error message. 
"""


def k_unique_substrings(given_string, k):
    if not k or not given_string:
        return None
    current_max = 0
    window = ""
    current_characters = set()
    longest_substrings = []
    for char in given_string:
        current_characters.add(char)
        window += char
        # If the set contains more than k, cleanup
        if len(current_characters) > k:
            if len(window[:-1]) > current_max:
                longest_substrings = []
                longest_substrings.append(window[:-1])
                current_max = len(window[:-1])
            elif len(window[:-1]) == current_max:
                longest_substrings.append(window[:-1])
            window_set = set()
            # Trim the window from the left
            for w in range(len(window)):
                window_set.add(window[w])
                if len(window_set) > 1:
                    current_characters.remove(window[w - 1])
                    window = window[w:]
                    break
    # If the remaining window is the same
    if len(window) >= current_max:
        longest_substrings.append(window)
    # If the remaining window is the largest
    if len(window) > current_max:
        longest_substrings = []
        longest_substrings.append(window)
    return longest_substrings


assert k_unique_substrings("aabbcc", k=1) == ["aa", "bb", "cc"]
assert k_unique_substrings("aabbccc", k=1) == ["ccc"]
assert k_unique_substrings("aaaabbccc", k=1) == ["aaaa"]
assert k_unique_substrings("aabbcc", k=2) == ["aabb", "bbcc"]
assert k_unique_substrings("aabbcc", k=3) == ["aabbcc"]
# Edge cases
assert k_unique_substrings("", k=3) == None
assert k_unique_substrings("abc", k=None) == None
