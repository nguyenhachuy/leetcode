class Solution:
    def palindrome_check(self, s, i,j):
        while i < j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True
    def validPalindrome(self, s: str) -> bool:
        i,j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return self.palindrome_check(s, i+1, j) or self.palindrome_check(s,i,j-1)
            i += 1
            j -= 1
        return True

def main():
    sol = Solution()
    print(sol.validPalindrome("aba"))
    print(sol.validPalindrome("abca"))
    print(sol.validPalindrome("a"))
    print(sol.validPalindrome(""))
    print(sol.validPalindrome("abdca"))
if __name__ == "__main__":
    main()

"""
when we find a mismatch, it must be palindrom if we skip this one, if not, we're over
abca
the mismatch creates 2 paths, skipping left, or skipping right

"""
