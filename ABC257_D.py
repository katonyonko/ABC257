import io
import sys

_INPUT = """\
6
4
-10 0 1
0 0 5
10 0 1
11 0 1
7
20 31 1
13 4 3
-10 -15 2
34 26 5
-2 39 4
0 -50 1
5 -20 2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import deque
  N=int(input())
  def connect(G):
    for i in range(N):
      used=[-1]*N
      used[i]=0
      dq=deque()
      dq.append(i)
      while dq:
        x=dq.popleft()
        for y in G[x]:
          if used[y]==0: continue
          used[y]=0
          dq.append(y)
      if sum(used)==0: return 1
    return 0
  jump=[list(map(int,input().split())) for _ in range(N)]
  l,r=0,10**10
  while r-l>1:
    mid=(l+r)//2
    G=[[] for _ in range(N)]
    for i in range(N):
      xi,yi,Pi=jump[i]
      for j in range(N):
        if i==j: continue
        xj,yj,Pj=jump[j]
        if Pi*mid>=abs(xi-xj)+abs(yi-yj): G[i].append(j)
    flg=connect(G)
    if flg==1: r=mid
    else: l=mid
  print(r)