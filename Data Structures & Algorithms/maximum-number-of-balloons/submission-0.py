class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        count = Counter(text)

        balloon_count = Counter("balloon")

        res = 0

        while count >= balloon_count:
            count = count - balloon_count
            res += 1

        return res