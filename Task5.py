# 5 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = float(input("Please type X: "))
y1 = float(input("Please type Y: "))
x2 = float(input("Please type X: "))
y2 = float(input("Please type Y: "))

D = round(((x1-x2)**2+(y1-y2)**2)**0.5,2)

print (D)

