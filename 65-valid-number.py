class Solution:
    def check_portion(self, s, i, j, sign_count, decimal_count, left):
        if i > j:
            return False
        num_count = 0
        for k in range(i,j+1):
            if s[k] == "+" or s[k] == "-":
                return False
            elif s[k] == ".":
                decimal_count += 1
                if decimal_count > 1:
                    return False
                if left and k == j and num_count > 0:
                    return True
                return self.check_portion(s, k+1,j,sign_count, decimal_count, False)
            elif s[k] == " ":
                return False
            elif not s[k].isdigit() and s[k].isalpha():
                return False
            else:
                num_count += 1
        return True
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s or s == ".":
            return False
        e_count = s.count("e")
        if e_count > 1:
            return False
        elif e_count == 0:
            if s[0] == "+" or s[0] == "-":
                return self.check_portion(s, 1, len(s)-1, 0, 0, True)
            else:
                return self.check_portion(s, 0, len(s)-1, 0, 0, True)
        else:
            e_index = s.index("e")
            left = 0
            if left < len(s) and (s[0] == "+" or s[0] == "-"):
                left += 1
            right = e_index + 1
            if right < len(s) and (s[right] == "+" or s[right] == "-"):
                right += 1


            return self.check_portion(s, left, e_index-1, 0, 0, True) and self.check_portion(s, right, len(s)-1, 0, 1, False)


"""
e split into 2
only 1 of +/-, can be for both sides
only decimal point on left
space trim on the sides, use strip

"""
def main():
    sol = Solution()
    strings = ["0", "0.1", "abc", "1 a", "2e10", "-90e3     ", " 1e", "e3", "  6e-1", " 99e2.5", "53.5e93", " --6", "-+3", "95e54e53", "."]
    for s in strings:
        print(s, ": ", sol.isNumber(s))

if __name__ == "__main__":
    main()

