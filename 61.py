a,b=map(int,input("請輸入遊戲時間:").split(":"))
time=a*60+b-75
wave=time//30+1
cs=wave*6+wave//3-wave//2
print(cs)