class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s, l, r):
            max_len = 0
            max_word = ""
            while l >= 0 and r < len(s) and s[l] == s[r]:
                new_len = r-l+1
                if new_len > max_len:
                    max_len = new_len
                    max_word = s[l:r+1]
                l -= 1
                r += 1
            return max_word
        
        result = ""
        for i in range(len(s)):
            single = expand(s, i,i)
            if len(single) > len(result):
                result = single
            double = expand(s, i, i+1)
            if len(double) > len(result):
                result = double
        
        return result