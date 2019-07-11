import random

def duplicadas(l):   # basicamente encontra todas as duplicadas e checa
   return len(l) != len([x for x in l for y in l if x==y])

def b_day(N,M,S):  # N: numero de aniversarios M: iterações, S: seed
  random.seed(S)  # reinicia o gerador randomico
  c=0
  for i in range(0,M):
    xs=[]
    for j in range(0,N):
      xs.append(random.randint(1,366))
    if duplicadas(xs):
      c+=1

  print N, M, c, c/float(M)
