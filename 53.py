a = {}
n=int(input("輸入 n 值:"))
for i in range(n):
    name = input("請輸入姓名:")
    e = input("請輸入電子郵件:")
    a[name] = e
s = input("請輸入要查詢電子郵件的姓名:")
print(f"{s} 電子郵件帳號為 {a[s]}")