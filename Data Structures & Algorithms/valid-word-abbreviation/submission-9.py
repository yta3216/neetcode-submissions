class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        i = 0
        j = 0

        while (i < len(word) and j < len(abbr)):
            if (abbr[j] == '0'):
                return False
            elif (abbr[j].isalpha()):
                if (word[i] is not abbr[j]):
                    return False
                i += 1
                j += 1

            elif (abbr[j].isnumeric()):
                total = ''
                while (j < len(abbr) and abbr[j].isnumeric()):
                    total += abbr[j]
                    j += 1
            
                i += int(total)
                print(total, i, j)

        if (i == len(word) and j == len(abbr)):
            return True
        else:
            return False