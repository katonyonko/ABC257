import io
import sys

_INPUT = """\
6
5
10101
60 45 30 40 80
3
000
1 2 3
5
10101
60 50 50 50 60
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  S=input()
  W=list(map(int,input().split()))
  key=sorted(list(set(W)))
  tmp=S.count('1')
  ans=tmp
  d={k:0 for k in key}
  for i in range(N):
    if S[i]=='0': d[W[i]]+=1
    else: d[W[i]]-=1
  for k in key:
    tmp+=d[k]
    ans=max(ans,tmp)
  print(ans)