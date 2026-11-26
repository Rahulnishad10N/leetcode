class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        n=len(intervals)

        ans = 0
        lastEnd = float('-inf')

        for start, end in intervals:
            if start >= lastEnd:
                ans += 1
                lastEnd = end

        return n-ans

        