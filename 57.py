x=input("請選擇主餐及升級的套餐:")
y=input("是否升級成大杯飲料:")
z=input("是否換成大薯:")
a=0
if x[1]=="A":
    if x[0] == "1":
      a+= 72 +55
    elif x[0] == "2":
        a += 62  +55
    elif x[0] == "3":
        a += 82 +55
    elif x[0] == "4":
        a += 44 +55
    elif x[0] == "5":
        a += 60 +55
elif x[1]=="B":
    if x[0] == "1":
      a+= 72 +68
    elif x[0] == "2":
        a += 62  +68
    elif x[0] == "3":
        a += 82 +68
    elif x[0] == "4":
        a += 44 +68
    elif x[0] == "5":
        a += 60 +68
if y =="是":
    a+=7
if z =="是":
    a+=13
print(f"總共為{a}元")    
        