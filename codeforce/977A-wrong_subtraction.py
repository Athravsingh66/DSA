n,k=map(int,input().split())
result=n
for _ in range(k):
    if result%10==0:
        result=result//10
    else:
        result-=1
print(result)
    