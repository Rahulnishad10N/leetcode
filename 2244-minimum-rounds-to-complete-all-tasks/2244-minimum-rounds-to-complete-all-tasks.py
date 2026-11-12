
class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        freq = {}

        for i in tasks:
            freq[i] = freq.get(i, 0) + 1

        ans = 0

        for i in freq:
            while freq[i] > 1:
                if freq[i] % 3 == 0:
                    ans += 1
                    freq[i] -= 3
                elif freq[i] % 3 == 1:
                    ans += 1
                    freq[i] -= 2
                else:
                    ans += 1
                    freq[i] -= 2

        for i in freq.values():
            if i != 0:
                return -1

        return ans
