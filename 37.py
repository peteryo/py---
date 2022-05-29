a=int(input("正整數:"))
while a!=1:
    if a%2==0:
        print(int(a),end=" ")
        a=a/2
    elif a%2!=0:
        print(int(a),end=" ")
        a=a*3+1
else:
    print(int(a),end=" ")