class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        st1 = []
        for c in S:
            if c == "#" and st1:
                st1.pop()
            elif c != "#":
                st1.append(c)
        st2 = []
        for c in T:
            if c == "#" and st2:
                st2.pop()
            elif c != "#":
                st2.append(c)
        return "".join(st1) == "".join(st2)
