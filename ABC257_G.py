import io
import sys

_INPUT = """\
6
aba
ababaab
atcoder
ac
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
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
  tmp=[i+tmp[i] for i in range(len(T))]
  key=set(tmp)
  d={k:10**10 for k in key}
  for i in range(len(T)):
    d[tmp[i]]=min(d[tmp[i]],i)
  key=sorted(list(key),reverse=True)
  ans=0
  now=key[0]
  next=d[key[0]]
  for i in range(len(key)):
    if key[i]<now:
      now=next
      ans+=1
    next=min(next,d[key[i]])
  if ans==0: print(-1)
  else: print(ans)