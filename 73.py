a,b,c=map(int,input("請輸入時間1(時:分:秒):").split(":"))
d=int(input("請輸入時間2(秒):"))
total1=a*3600+b*60+c
a1=d//3600
b1=(d-a1*3600)//60
c1=d-a1*3600-b1*60
print(total1)
print(f"{a1}:{b1}:{c1}")