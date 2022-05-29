a={}
n=int(input("輸入比數n:"))
for i in range(n):
    b,c=input().split()
    a[b]=c
s=input("輸入欲查詢單字:")
if s in a:
    print(f"{s}中文意思為{a[s]}")
else:
    print("字典未有此單字")