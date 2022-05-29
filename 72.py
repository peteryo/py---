n=int(input("請輸入n:"))
k=int(input("請輸入k:"))
pi=n//k
total=pi
while pi>=k:
    if pi>=k:
        pi=pi//k
        total+=pi
    else :
        break
print(f"peter可以抽{n+total}支紙菸")        