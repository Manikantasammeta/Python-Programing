def longest_unique_substring(s):
    seen = {}
    left = 0
    max_len = 0
    
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        max_len = max(max_len, right - left + 1)
    
    return max_len

print(longest_unique_substring("abcabcbb"))  # Output: 3
print(longest_unique_substring("bbbbb"))     # Output: 1
