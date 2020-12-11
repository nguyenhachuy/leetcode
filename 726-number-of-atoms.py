from collections import defaultdict

class Solution:
    def rcs(self, s, i):
        if i < 0:
            return (-1, {})
        factor = 1
        result = defaultdict(int)
        while i >= 0:
            if s[i] == ")":
                new_index, table = self.rcs(s, i-1)
                i = new_index
                for c in table:
                    result[c] += table[c]*factor
                factor = 1
            elif s[i].islower():
                j = i
                while j >= 0 and s[j].islower():
                    j -= 1
                atom_name = s[j:i+1]
                result[atom_name] += factor
                factor = 1
                i = j
            elif s[i].isupper():
                result[s[i]] += factor
                factor = 1
            elif s[i].isdigit():
                j = i
                while j >= 0 and s[j].isdigit():
                    j -= 1
                factor = int(s[j+1:i+1])
                i = j + 1
            elif s[i] == "(":
                return (i, result)
            i -= 1
        return (i, result)

    def countOfAtoms(self, formula: str) -> str:
        result = self.rcs(formula, len(formula) - 1)[1]
        s = ""
        for key in sorted(result.keys()):
            s += key
            if result[key] > 1:
                s += str(result[key])
        return s

def main():
    sol = Solution()
    print(sol.countOfAtoms("H2O"))
    print(sol.countOfAtoms("Mg(OH)2"))
    print(sol.countOfAtoms("K4(ON(SO3)2)2"))
    print(sol.countOfAtoms("Be32"))
if __name__ == "__main__":
    main()

