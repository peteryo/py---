a={}
x=int(input("輸入比數n:"))
for i in range(x):
    pie,num=input().split()
    a[pie]=num
for pie in a:
    print(f"{pie}牌得到{a[pie]}面")    