class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mm = {}
        ss = ""
        if s == "":
            return 0
        for w in s:
            if w not in ss:
                ss += w
            else:
                ss = ss[ss.index(w) + 1 :] + w
            mm[ss] = len(ss)
        return max(mm.values())
