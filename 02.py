a=float(input("輸入度數:"))
if a<=120:
    print("summer months:",a*2.10)
    print("non-summer months:",a*2.10)
elif a<=330 : 
    print("summer months:",120*2.10+(a-120)*3.02)
    print("non-summer months:",120*2.10+(a-120)*2.68) 
elif a<=500 : 
    print("summer months:",120*2.10+210*3.02+(a-330)*4.39)
    print("non-summer months:",120*2.10+210*2.68+(a-330)*3.61) 
elif a<=700 : 
    print("summer months:",120*2.10+210*3.02+170*4.39+(a-500)*4.97)
    print("non-summer months:",120*2.10+210*2.68+170*3.61+(a-500)*4.01) 
else  : 
    print("summer months:",120*2.10+210*3.02+170*4.39+200*4.97+(a-700)*5.63)
    print("non-summer months:",120*2.10+210*2.68+170*3.61+200*4.01+(a-700)*4.50) 