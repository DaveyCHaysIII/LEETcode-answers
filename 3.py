"""
3. Longest substring without repeated characters

(desc is title)
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_dict = {}
        slen = 0
        temp = 0

        if not s:
            return 0

        for i in range(len(s)):
            if s[i] in char_dict and char_dict[s[i]] >= temp:
                temp = char_dict[s[i]] + 1
            char_dict[s[i]] = i
            slen = max(slen, i - temp + 1)
        return slen

"""
Hard part: edge cases ruined me, had to look up final iteration
(mainly the char_dicts[s[i]] >= temp line)

Strategy: make a counter for "streak" and update a var when it
breaks that streak

Answer: optimal, because I referenced it

Time Complexity: ON

Better solution: already optimal
"""


