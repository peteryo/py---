a=int(input("班級數量:"))
ans=0
for i in range(a):
    s=int(input())
    if s > ans :
        ans=s
print("電腦數量:",ans)