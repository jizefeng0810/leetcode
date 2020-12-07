class Solution:
    def minWindow(self, s: str, t: str):
        # if len(t) == 1 and t in s:
        #     return t
        need, window = {}, {}
        for c in t:
            window[c] = 0
            if c in need.keys():
                need[c] += 1
            else:
                need[c] = 1
        left, right = 0, 0
        valid = 0
        start, length = 0, 10000000
        while right < len(s):
            c = s[right]
            right += 1
            if c in need.keys():
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            while valid == len(need):
                if right - left < length:
                    start = left
                    length = right - left
                d = s[left]
                left += 1
                if d in need.keys():
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        if length == 10000000:
            return ''
        else:
            return s[start:start+length]

if __name__=='__main__':
    s = "ADOBECODEBANC"
    t = "ABC"           # "BANC"
    s = "a"
    t = "a"             # "a"
    solution = Solution()
    result = solution.minWindow(s,t)
    print(result)
