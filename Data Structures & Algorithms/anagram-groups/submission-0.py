class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        
        for s in strs:
            key = "".join(sorted(s))
            if (hash.get(key) == None):
                hash[key] = []
            hash[key].append(s)
        return list(hash.values())
            
