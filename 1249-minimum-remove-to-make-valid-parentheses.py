class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s_arr = list(s)
        balance = 0
        for i,c in enumerate(s_arr):
            if c != "(" and c != ")":
                continue

            if c == "(":
                balance += 1
            elif c == ")":
                balance -= 1
            if balance < 0:
                s_arr[i] = ""
                balance += 1

        if balance > 0:
            for i in reversed(range(len(s_arr))):
                if balance == 0:
                    break
                if s_arr[i] == "(":
                    balance -= 1
                    s_arr[i] = ""

        return "".join(s_arr)

def main():
    sol = Solution()
    print(sol.minRemoveToMakeValid("lee(t(c)o)de)"))
    print(sol.minRemoveToMakeValid("a)b(c)d"))
    print(sol.minRemoveToMakeValid("))(("))
    print(sol.minRemoveToMakeValid("(a(b(c)d)"))

if __name__ == "__main__":
    main()


"""
calculate deficit -> O(n)
))(
(()()) -> 0 no
lee(t(c)o)de)
a)b(c)d -> remove first one is not valid
deficit at any point should be 0
if positive

if 0 to negative, all must be removed
if positive to negative, remove any extra negative and fix on the spot
if positive stay positive, go one extra round to remove any )

"""
