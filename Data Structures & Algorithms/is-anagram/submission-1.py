class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        hashmap = defaultdict(int)
        for c in s:
            hashmap[c] += 1
        for c2 in t:
            if (hashmap[c2] == 0):
                return False
            hashmap[c2] -= 1
        
        for item, val in hashmap.items():
            if val != 0:
                return False
        return True