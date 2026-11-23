class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = [0] * 52

        for ch in s:
            if ch.islower():
                idx = ord(ch) - ord('a')
            else:
                idx = ord(ch) - ord('A') + 26

            freq[idx] += 1

        odd = False
        ans = 0

        for i in freq:
            if i > 0:
                if i % 2:
                    odd = True

                ans += 2 * (i // 2)

        return ans + 1 if odd else ans