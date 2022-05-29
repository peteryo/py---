a=float(input("請輸入路程公里數:(km):"))
a=a*1000
if a<=1500:
    print("所需車資為:75")
else:
    if (a-1500)%250==0:
        money=(a-1500)//250*5+75
        print(int(money))
    else:
        money=(a-1500)//250*5+80
        print(int(money))   
