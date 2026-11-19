class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        checksum = Counter(s1)

        l = 0
        diff = {}
        for i in range(0, len(s2) - len(s1) + 1):
            print(checksum)
            print(Counter(s2[i:(i+len(s1))]))
            if checksum == Counter(s2[i:(i+len(s1))]):
                return True
        return False