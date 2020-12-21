class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        reverse_str = s[::-1]
        if s == reverse_str:
            return s
        for i in reversed(range(len(s))):
            if s[:i] == reverse_str[len(s) - i:]:
                # print(s[:i], reverse_str[len(s) - i:])
                return reverse_str[:len(s) - i] + s
        return s

def main():
    sol = Solution()
    strings = [
        "aacecaaa",
        "abcd",
        "",
        "b",
        "lls",
        "acbcaa"
    ]
    for s in strings:
        print(sol.shortestPalindrome(s))
if __name__ == "__main__":
  main()



