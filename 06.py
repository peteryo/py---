num=input("輸入值為:").split(",")
a=sorted(num)
b=sorted(num,reverse=True)
big=int("".join(b))
min=int("".join(a))
print("最大值數列與最小值數列差值為:"+str(big-min))