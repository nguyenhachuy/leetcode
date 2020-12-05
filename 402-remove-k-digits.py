class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for i,v in enumerate(num):
            while st and int(st[-1]) > int(v) and k > 0:
                st.pop()
                k-=1
            st.append(v)
        zero_index = 0
        while zero_index < len(st) and st[zero_index] == "0":
            zero_index += 1
        st = st[zero_index:]
        if k:
            return "".join(st[:-k]) or "0"
        return "".join(st)


def main():
  num = "10"
  sol = Solution()
  print(sol.removeKdigits(num, 2))

if __name__ == "__main__":
  main()
