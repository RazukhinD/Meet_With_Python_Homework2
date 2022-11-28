number=int(input('Введи число N чисел которые будут в последовательности: '))
new_list=[]
sum=0
for i in range(1,number+1):
    element = (1+1/i)**i
    new_list.append(element)
    sum+=element
print(new_list)
print(sum)

