import heapq

class Word(str):
    def __lt__(self, other):
        return self > other

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        mp = {}
        heap = []

        for i in words:
            mp[i] = mp.get(i, 0) + 1

        for word, freq in mp.items():
            heapq.heappush(heap, (freq, Word(word)))

            if len(heap) > k:
                heapq.heappop(heap)

        ans = []

        while heap:
            freq, word = heapq.heappop(heap)
            ans.append(str(word))

        return ans[::-1]