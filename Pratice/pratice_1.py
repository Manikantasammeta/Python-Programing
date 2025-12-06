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




def majority_element(nums):
    count, candidate = 0, None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate

print(majority_element([3,3,4,2,3,3,5]))  # Output: 3




# Prime Factors of a given number 
n=10 
i=1
while i<=n:
    if n%i==0:
        for j in range(2,i//2):
            if i%j==0:
                break
        else:
            print(i)
    i+=1
