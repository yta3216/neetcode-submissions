class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        res = float('inf')
        actions = 0
        l = 0

        for r in range(len(blocks)):
            if (l + r + 1 > k):
                if (blocks[l] == "W"):
                    actions -= 1
                l += 1
            
            if (blocks[r] == "W"):
                actions += 1

            if (l + r + 1 >= k):
                res = min(res, actions)

        return res
            