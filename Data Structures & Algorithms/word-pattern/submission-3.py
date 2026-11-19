class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hm = {}
        hm = defaultdict(str)
        strings = s.split(" ")
        words = {}
        words = defaultdict(str)

        if len(strings) != len(pattern):
            return False

        for i in range(len(pattern)):

            if not hm[pattern[i]]:
                hm[pattern[i]] = strings[i]
                if not words[strings[i]]:
                    words[strings[i]] = 1
                else:
                    return False
                continue

            if hm[pattern[i]] != strings[i]:
                return False
        return True