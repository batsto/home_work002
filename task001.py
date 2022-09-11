# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 
#Учтите, что числа могут быть отрицательными

#Пример:

# 67.82 -> 23
#0.56 -> 11      



from curses.ascii import isdigit


numbers = input()
sum = 0
x = list(numbers)
for i in x:
    if isdigit(i) == True:
        sum += int(i)

print(sum)
print(x)