import io
import sys

_INPUT = """\
6
1 3
2 12
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,X=map(int,input().split())
  print(chr((X-1)//N+ord('A')))