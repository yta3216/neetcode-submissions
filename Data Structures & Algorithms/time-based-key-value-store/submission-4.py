class TimeMap:
    def __init__(self):
        self.hm = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        curr_key = self.hm[key]
        if not curr_key or timestamp < curr_key[0][1]:
            return ""

        r = len(curr_key) - 1
        l = 0
        while (l <= r):
            m = l + (r - l) // 2
            if (curr_key[m][1] > timestamp):
                r = m - 1
            elif (curr_key[m][1] < timestamp):
                l = m + 1
            else:
                return curr_key[m][0]
        return curr_key[r][0]
