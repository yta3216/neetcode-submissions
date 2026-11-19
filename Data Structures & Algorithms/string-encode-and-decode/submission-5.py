class Solution:
    delimiter = "#"
    
    # delimiter format: length of string + delimiter
    # e.g.: i = "hi" -> delim = "2#", out = "2#hi"
    def encode(self, strs: List[str]) -> str:
        output = ""
        for i in strs:
            output += str(len(i)) + self.delimiter + i 
        return output

    def decode(self, s: str) -> List[str]:
        remaining = s
        r = 1
        out = []
        while remaining:
            if (remaining[r] == self.delimiter):
                i = int(remaining[:r])
                low = r + 1 # add 1 to skip delimiter
                high = low + i
                out.append(remaining[low:high])
                remaining = remaining[high:]

                r = 1
            else:
                r += 1

        return out


                
            
            
        