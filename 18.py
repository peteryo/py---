a=input().split()
p13={"A":1,"J":11,"Q":12,"K":13}
total=0
for i in a:
    if i in p13:
        total+=p13[i]
    else:
        total+=int(i)
print(total)    