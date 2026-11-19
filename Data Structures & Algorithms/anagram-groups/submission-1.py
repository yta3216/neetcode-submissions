class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        for s in strs:
            key = "".join(sorted(s)) # treat sorted string as hash
            if hm.get(key) == None: # compare against existing hm
                hm[key] = [] # add new list if unique
            hm[key].append(s) # append if not
                
        return list(hm.values())