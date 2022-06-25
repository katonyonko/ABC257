import io
from multiprocessing.connection import answer_challenge
import sys

_INPUT = """\
6
3 2
0 2
1 2
5 5
1 2
1 3
3 4
4 5
0 2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import deque
  def bfs(G,s):
    inf=10**30
    D=[inf]*len(G)
    D[s]=0
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if D[y]>D[x]+1:
          D[y]=D[x]+1
          dq.append(y)
    return D
  N,M=map(int,input().split())
  G=[[] for _ in range(N+1)]
  for i in range(M):
    U,V=map(int,input().split())
    G[U].append(V)
    G[V].append(U)
  D1,DN=bfs(G,1),bfs(G,N)
  ans=[]
  for i in range(1,N+1):
    tmp=min(D1[N],D1[0]+DN[i],D1[i]+DN[0])
    if tmp==10**30: ans.append(-1)
    else: ans.append(tmp)
  print(*ans)