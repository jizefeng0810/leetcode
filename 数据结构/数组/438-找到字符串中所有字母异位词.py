class Solution:
    def findAnagrams(self, s2: str, s1: str):
        need, window = {}, {}
        for c in s1:
            window[c] = 0
            if c in need.keys():
                need[c] += 1
            else:
                need[c] = 1
        left, right = 0, 0
        valid = 0
        res = []
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in need.keys():
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            while right - left >= len(s1):
                if valid == len(need):
                    res.append(left)
                d = s2[left]
                left += 1
                if d in need.keys():
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return res

if __name__=='__main__':
    s = "cbaebabacd"
    p = "abc"           # [0, 6]
    # s = "abab"
    # p = "ab"           # [0, 1, 2]
    solution = Solution()
    result = solution.findAnagrams(s, p)
    print(result)
