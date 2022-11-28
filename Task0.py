number=input('Введи число сумму цифр которого надо посчитать: ')
sum = 0
for i in number:
    if i.isdigit():
        sum+=int(i)
print(sum)


