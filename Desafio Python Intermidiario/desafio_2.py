
T = int(input())

for i in range(T):
    N, K = int(input())
    total = N
    while N >= K:
      troca = N // K
      N = troca + (N % K)
      total += troca