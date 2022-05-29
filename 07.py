a,b=map(int,input("輸入月租費型式及通話時間(以逗點隔開):").split(","))
x={186:0.09,386:0.08,586:0.07,986:0.06}
for i in x :
    if a == i:
        ans=b*x[i]
        ans*=x[i]*10-0.1 if b * x[i]>a else x[i]*10
print("通話費為:%.0f"%ans)
