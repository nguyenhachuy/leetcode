class Solution:
    def DFS(self, s, i):
        if i >= len(s):
            return ''
        pattern = ''
        while i < len(s):
            if s[i] == ']':
                return pattern
            elif s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num *= 10
                    num += int(s[i])
                    i+=1
                suffix = self.DFS(s, i)
                brackets = 1
                i = i + 1
                while brackets > 0 and i < len(s):
                    if s[i] == ']':
                        brackets -= 1
                    elif s[i] == '[':
                        brackets += 1
                    i += 1
                pattern += num * suffix
            elif s[i] != '[':
                pattern += s[i]
                i += 1
            else:
                i += 1

        return pattern

    def decodeString(self, s: str) -> str:
        return self.DFS(s, 0)

def main():
    sol = Solution()
    print(sol.decodeString("3[a]2[bc]"))
    print(sol.decodeString("3[a2[c]]"))
    print(sol.decodeString("2[abc]3[cd]ef"))
    print(sol.decodeString("abc3[cd]xyz"))
    print(sol.decodeString("100[leetcode]"))
if __name__ == "__main__":
  main()
