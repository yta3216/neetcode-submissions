class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = defaultdict(int)
        for i in s:
            l[i] += 1
        for i in t:
            if (l.get(i) == None or l.get(i) == 0):
                return False
            l[i] -= 1
            if (l.get(i) == 0):
                l.pop(i)
        if not l:
            return True
        else:
            return False