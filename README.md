# Regular Expression Matching

This repository contains a solution for the regular expression matching problem, which checks if an input string `s` matches a given pattern `p` that supports the special characters `.` and `*`.

## Problem Statement

Implement regular expression matching with support for:

- `.`: Matches any single character.
- `*`: Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

### Examples

1. **Example 1:**

   - **Input:** `s = "aa"`, `p = "a"`
   - **Output:** `false`
   - **Explanation:** "a" does not match the entire string "aa".

2. **Example 2:**

   - **Input:** `s = "aa"`, `p = "a*"`
   - **Output:** `true`
   - **Explanation:** `'*'` means zero or more of the preceding element, `'a'`. Therefore, by repeating `'a'` once, it becomes "aa".

3. **Example 3:**
   - **Input:** `s = "ab"`, `p = ".*"`
   - **Output:** `true`
   - **Explanation:** "._" means "zero or more (`_`) of any character (`.
