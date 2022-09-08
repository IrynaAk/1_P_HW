# 4 Напишите программу, которая по заданному номеру четверти, показывает 
# диапазон возможных координат точек в этой четверти (x и y).

q = int(input("Please type quarter number (from 1 to 4): "))

if q==1:
    print('x>0 and y>0')
elif q==2:
    print("x<0 and y>0")
elif q==3:
    print("x<0 and y<0")
elif q==4:
    print("x>0 and y<0")
else:
    print("the value is incorrect")