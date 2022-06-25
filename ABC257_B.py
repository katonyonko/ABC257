import io
import sys

_INPUT = """\
6
5 3 5
1 3 4
3 3 1 1 2
2 2 2
1 2
1 2
10 6 9
1 3 5 7 8 9
1 2 3 4 5 6 5 6 2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,K,Q=map(int,input().split())
  A=list(map(lambda x: int(x)-1,input().split()))
  L=list(map(lambda x: int(x)-1,input().split()))
  for i in range(Q):
    if A[L[i]]==N-1: continue
    else:
      if L[i]<K-1 and A[L[i]+1]==A[L[i]]+1: continue
      else:
        A[L[i]]+=1
  print(*map(lambda x: int(x)+1,A))