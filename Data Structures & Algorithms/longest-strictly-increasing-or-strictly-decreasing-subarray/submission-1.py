class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        

        inc = 1
        curr_inc = 1
        dec = 1
        curr_dec = 1

        prev = None
        
        for i in nums:
            if not prev:
                prev = i
                continue


            if (prev > i):
                inc = max(inc, curr_inc)
                curr_inc = 1
                curr_dec += 1

            elif (prev < i):
                dec = max(dec, curr_dec)
                curr_dec = 1
                curr_inc += 1

            else:
                inc = max(inc, curr_inc)
                dec = max(dec, curr_dec)
                curr_inc = 1
                curr_dec = 1
            print(curr_inc)
            print(curr_dec)
            prev = i
        return max(curr_inc, curr_dec, inc, dec)