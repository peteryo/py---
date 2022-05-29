m=int(input("小明身上有幾元:"))
n=int(input("販賣機有幾種飲料:"))
x=0
for i in range(n):
    a=int(input())
    if m>=a:
        x+=1
print(x)
