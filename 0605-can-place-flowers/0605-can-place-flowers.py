class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        m = len(flowerbed)

        if n == 0:
            return True

        for i in range(m):
            if flowerbed[i] != 1:

                if i == 0:
                    if m == 1 or flowerbed[i+1] == 0:
                        n -= 1
                        flowerbed[i] = 1

                elif i == m-1:
                    if flowerbed[i-1] == 0:
                        n -= 1
                        flowerbed[i] = 1

                else:
                    if flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                        n -= 1
                        flowerbed[i] = 1

                if n <= 0:
                    return True

        return False