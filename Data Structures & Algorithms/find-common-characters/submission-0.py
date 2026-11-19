class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        hm = Counter(words[0])

        for i in range(len(words)):
            hm = hm & Counter(words[i])
        print(hm)
        return list(hm.elements())