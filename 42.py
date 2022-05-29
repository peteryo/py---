a = int(input())
b = int(input())
c = int(input())

D = b**2 - 4*a*c
if D > 0:
    print("x=",int((-b + pow(b**2 - 4*a*c,0.5))/(2*a)))
    print("x=",int((-b - pow(b**2 - 4*a*c,0.5))/(2*a)))
elif D == 0:
    print("x=",int(-b / (2*a)))
else:
    print("x=無解")