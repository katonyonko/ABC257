import io
import sys

_INPUT = """\
6
aba
ababaab
atcoder
ac
atcoder
ba
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  #Segment Tree
  class SegTree:
      X_unit = 1 << 30
      X_f = min

      def __init__(self, N):
          self.N = N
          self.X = [self.X_unit] * (N + N)

      def build(self, seq):
          for i, x in enumerate(seq, self.N):
              self.X[i] = x
          for i in range(self.N - 1, 0, -1):
              self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

      def set_val(self, i, x):
          i += self.N
          self.X[i] = x
          while i > 1:
              i >>= 1
              self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

      def fold(self, L, R):
          L += self.N
          R += self.N
          vL = self.X_unit
          vR = self.X_unit
          while L < R:
              if L & 1:
                  vL = self.X_f(vL, self.X[L])
                  L += 1
              if R & 1:
                  R -= 1
                  vR = self.X_f(self.X[R], vR)
              L >>= 1
              R >>= 1
          return self.X_f(vL, vR)
  def z_algorithm(s):
    N = len(s)
    Z_alg = [0]*N
    Z_alg[0] = N
    i = 1
    j = 0
    while i < N:
        while i+j < N and s[j] == s[i+j]:
            j += 1
        Z_alg[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i+k < N and k + Z_alg[k]<j:
            Z_alg[i+k] = Z_alg[k]
            k += 1
        i += k
        j -= k
    return Z_alg
  S=input()
  T=input()
  tmp=z_algorithm(S+'_'+T)[-len(T):]
  tmp=[tmp[i] for i in range(len(T))]
  sg=SegTree(len(T)+1)
  sg.build([10**10 if i <len(T) else 0 for i in range(len(T)+1)])
  for i in range(len(T)):
    sg.set_val(len(T)-i-1,sg.fold(len(T)-i,len(T)-i+tmp[len(T)-i-1])+1)
  ans=sg.fold(0,1)
  if ans==1<< 30: print(-1)
  else: print(ans)