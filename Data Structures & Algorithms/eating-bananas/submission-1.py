class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        k_upper = max(piles)
        k_lower = 1
        res = k_upper

        while k_lower <= k_upper:
            total = 0
            k = k_lower + (k_upper - k_lower) // 2

            for i in piles:
                total += -math.ceil( i // - k)

            if (total <= h):
                k_upper = k - 1
                res = min(k, res)
            elif (total > h):
                k_lower = k + 1
        return res