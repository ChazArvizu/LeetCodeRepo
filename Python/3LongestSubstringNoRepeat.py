"""
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        chars = set()
        count = 0
        max_count = 0
        start = 0

        for char in s:

            if char not in chars:
                chars.add(char)
                count += 1
                max_count = max(max_count, count)

            else:
                while s[start] != char:
                    chars.remove(s[start])
                    start += 1
                    count -= 1
                start += 1

        return max_count
