class Solution:
    delimiter = "#"
    def encode(self, strs: List[str]) -> str:
        # using "#" as a delimiter

        buf = ""
        for i in strs:
            buf += str(len(i)) + self.delimiter + i
        return buf

    def decode(self, s: str) -> List[str]:
        print(s)
        l = []
        buf = ""
        count = 0
        reading = True
            

        for i in s:
            if (reading):
                if (i != self.delimiter):
                    buf += i
                else: 
                    count += int(buf)
                    buf = ""
                    reading = False
                    if count == 0:
                        l.append(buf)
                        reading = True
            else:
                buf += i
                count -= 1
                if (count == 0):
                    l.append(buf);
                    buf = ""
                    reading = True
        return l
