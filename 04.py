x=int(input("x軸座標:"))
y=int(input("y軸座標:"))
z=x*x+y*y
if x>0 and y>0 :
    print("該點位於第一象限，離原點距離為根號",z)
elif x<0 and y>0 :
    print("該點位於第二象限，離原點距離為根號",z)
elif x<0 and y<0 :
    print("該點位於第三象限，離原點距離為根號",z)
elif x>0 and y<0 :
    print("該點位於第四象限，離原點距離為根號",z)
elif x==0 and y>0 :
    print("該點位於上半平面Y軸上，離原點距離為根號",z)
elif x==0 and y<0 :
    print("該點位於下半平面Y軸上，離原點距離為根號",z)
elif x>0 and y==0 :
    print("該點位於上半平面X軸上，離原點距離為根號",z)
elif x<0 and y==0 :
    print("該點位於下半平面X軸上，離原點距離為根號",z)
else :
    print("該點位於原點")
