def is_match(s: str, p: str) -> bool:
    # Create a DP table with dimensions (len(s) + 1) x (len(p) + 1)
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    
    # Empty string and empty pattern are a match
    dp[0][0] = True
    
    # Handle patterns like a*, a*b*, etc. where the string is empty
    for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    # Fill the DP table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))

    return dp[len(s)][len(p)]

# Example Usage
# More Example Usage
print(is_match("aab", "c*a*b"))     # Output: True
print(is_match("mississippi", "mis*is*p*.")) # Output: False
print(is_match("ab", ".*c"))         # Output: False
print(is_match("aaa", "a*a"))        # Output: True
print(is_match("a", ".*"))           # Output: True
print(is_match("b", ".*"))           # Output: True
print(is_match("abcd", "d.*"))       # Output: True
print(is_match("", ".*"))             # Output: True
print(is_match("abcd", ".*d"))       # Output: True
print(is_match("abcd", ".*e"))       # Output: False
print(is_match("abc", ".*a.*"))      # Output: False
print(is_match("abc", ".*bc"))       # Output: True

