
# 1 Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

a = int(input("Please type a numbre from 1 to 7: "))

if a>0 and a<6:
    print('this is a worday')
elif a == 6 or a == 7:
    print("this is a weekend")
else:
    print("the value is not from 1-7 range")


