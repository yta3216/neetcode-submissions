class Solution:
    def numDecodings(self, s: str, memo=None) -> int:
        if memo is None:
            memo = {}
        if s == "":
            return 1
        if s in memo:
            return memo[s]
        ways = 0
        if int(s[-1]) >= 1 and int(s[-1]) <= 9:
            ways += self.numDecodings(s[:-1], memo)
        if len(s) >= 2 and s[-2] != "0" and int(s[-2:]) >= 1 and int(s[-2:]) <= 26:
            ways += self.numDecodings(s[:-2], memo)
        memo[s] = ways
        return memo[s]
            