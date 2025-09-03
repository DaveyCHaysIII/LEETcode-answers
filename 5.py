"""
5. Longest Palindromic substring

(desc is title)
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        start, maxLen = 0, 1

        for i in range(n):
            for j in range(2):
                low, high = i, i + j

                while low >= 0 and high < n and s[low] == s[high]:
                    currLen = high - low + 1
                    if currLen > maxLen:
                        start = low
                        maxLen = currLen
                    low -= 1
                    high += 1
        return s[start:start + maxLen]

"""
Hard parts: had no idea how to even approach this one, though I did
throw away some of my solutions I second guessed. Maybe I should trust
my instincts enough to at least try.

I threw away an idea to write a helper function to test if a range is
pallindromic, which was included in a lot of the example code I saw. I think
breaking this problem down into smaller problems would have been a better approach.

I not only didn't write this solution, I still don't really understand it. This feels like
clever programming at its worst. I like making things that just work, and referencing the
clever bits along the way.

Strategy: didn't even get that far, completely stole this answer

Answer: our referenced answer is good, but its not optimal! Out of many strategies to
solve pallindromic problems, we chose the expansion from center solution. There's an even
cleverer solution using Manacher's algorithm, which is an algorithm to do exactly this problem
(though its real world use cases only exist with incredibly long strings where we care about
 the existence of pallindromes)

class manacher:
    # p[i] stores the radius of the palindrome
    # centered at position i in ms

    def __init__(self, s):
        # transformed string with sentinels
        # and separators
        self.ms = "@"
        for c in s:
            self.ms += "#" + c
        self.ms += "#$"
        self.p = [0] * len(self.ms)
        self.runManacher()

    def runManacher(self):
        n = len(self.ms)
        l = r = 0

        for i in range(1, n - 1):
            mirror = l + r - i
            if 0 <= mirror < n:
                self.p[i] = max(0, min(r - i, self.p[mirror]))
            else:
                self.p[i] = 0

            # try expanding around center i
            while (i + 1 + self.p[i] < n and
                   i - 1 - self.p[i] >= 0 and
                   self.ms[i + 1 + self.p[i]] == self.ms[i - 1 - self.p[i]]):
                self.p[i] += 1

            # update [l, r] if the new palindrome goes
            # beyond current right boundary
            if i + self.p[i] > r:
                l = i - self.p[i]
                r = i + self.p[i]

    # return the radius of the longest palindrome
    # centered at original index 'cen'
    def getLongest(self, cen, odd):
        pos = 2 * cen + 2 + (0 if odd else 1)
        return self.p[pos]

    # checks whether the substring
    # s[l..r] is a palindrome
    def check(self, l, r):
        length = r - l + 1
        return length <= self.getLongest((l + r) // 2, length % 2)


# finds and returns the longest
# palindromic substring in s
def getLongestPal(s):
    n = len(s)
    maxLen = 1
    start = 0
    M = manacher(s)

    for i in range(n):
        oddLen = M.getLongest(i, 1)
        if oddLen > maxLen:
            # update start for odd-length palindrome
            start = i - (oddLen - 1) // 2

        evenLen = M.getLongest(i, 0)
        if evenLen > maxLen:
            # update start for even-length palindrome
            start = i - (evenLen - 1) // 2

        maxLen = max(maxLen, max(oddLen, evenLen))

    return s[start:start + maxLen]

"""
