from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        i = 0
        j = 0
        while i < len(s2):
            if s2[i] in s1_counter:
                s1_counter[s2[i]] -= 1
                while j < i and s1_counter[s2[i]] < 0:
                    if s2[j] in s1_counter:
                        s1_counter[s2[j]] += 1

                    j += 1
            else:
                while j <= i:
                    if s2[j] in s1_counter:
                        s1_counter[s2[j]] += 1
                    j += 1
            if i-j+1 == len(s1):
                return True
            i += 1
        return False

def main():
    sol = Solution()
    print(sol.checkInclusion("ab", "eidbaooo"))
    print(sol.checkInclusion("ab", "eidboaoo"))
    print(sol.checkInclusion("idboaoo", "eidboaoo"))
    print(sol.checkInclusion("acd", "dcda"))
    print(sol.checkInclusion("aa", "annaa"))
if __name__ == "__main__":
  main()
