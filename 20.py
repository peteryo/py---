n=int(input("組數為:"))
money=[]
for i in range(1,n+1):
    a,b=map(int,input(f"第{i}組:").split())
    money.append(a*250+b*175)
print()
for j in range(1,n+1):
    print(f"第{j}組應收費用:{money[j-1]}")    

