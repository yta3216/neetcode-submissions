class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)):
            return False

        l = 0

        for i in range(len(s1), len(s2)+1):
            print(s2[l:i])
            if (Counter(s1) == Counter(s2[l:i])):
                return True
            l += 1

        return False
        