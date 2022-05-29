a=input("請輸入一串小寫英文:")
b=["a","e","i","o","u"]
c=""
for i in a:
    if i in b :
        c+="."
    else :
        c+=i
print(c)            