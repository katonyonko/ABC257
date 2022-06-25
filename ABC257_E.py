import io
import sys

_INPUT = """\
6
5
5 4 3 3 2 5 3 5 3
20
1 1 1 1 1 1 1 1 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  C=list(map(int,input().split()))
  x=min(C)
  keta=N//x
  amari=N-N//x*x
  ans=[0]*9
  for i in reversed(range(9)):
    if C[i]==x: ans[i]=keta; break
    else:
      ans[i]=amari//(C[i]-x)
      amari-=amari//(C[i]-x)*(C[i]-x)
      keta-=ans[i]
  print(*[str(i+1)*ans[i] for i in reversed(range(9))],sep='')