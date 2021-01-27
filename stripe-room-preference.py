class Solution:
    def __init__(self, wishlish):
        self.wishlish = wishlish
    def both_first_rank(self, A,B):
        return self.both_n_th_rank(A,B,0)
    def both_n_th_rank(self, A,B, rank):
        if not self.wishlish[A] or len(self.wishlish[A]) < rank
            or not self.wishlish[B] or len(self.wishlish[B]) < rank:
            return False
        return self.wishlish[A][rank-1] == B and self.wishlish[B][rank-1] == A
