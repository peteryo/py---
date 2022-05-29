a=int(input("搭了幾次電梯:"))
f=1
money=0
for i in range(a):
    b=int(input())
    if b > f:
        money+=(b-f)*20
    elif b<f:
        money+=(f-b)*10
    f=b
print(f"{money}元")            
