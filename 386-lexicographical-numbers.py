class Solution:
    def rcs(self, i, n):
        if i > n:
            return []
        result = [i] + self.rcs(i*10,n)
        if i % 10 == 9:
            return result
        else:
            return result + self.rcs(i+1,n)


    def lexicalOrder(self, n: int) -> List[int]:
        return self.rcs(1,n)
