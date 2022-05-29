m=int(input("請輸入階層值M:"))
n=1
a=1
while a<m:
    n+=1
    a*=n
print(f"超超過M為{m}的最小階層N值為:{n}")