class Solution(object):
    def lengthOfLongestSubstring(self, s):
        chars = ""
        max_len = 0

        for ch in s:
            if ch in chars:
                chars = chars[chars.index(ch) + 1:]

            chars += ch
            max_len = max(max_len, len(chars))

        return max_len