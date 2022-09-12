# 3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.

N = int(input())

def revers_number(n):
    temporary = 0
    array = list(str(N))
    for i in range(len(array)//2):
        temporary = array[i]
        array[i] = array[len(array)-i-1]
        array[len(array)-i-1] = temporary
    temp = ''
    for x in range(len(array)):
        temp += array[x]
    return int(temp)
print(revers_number(N))

def polindrom_namber(n): 
    while(n != revers_number(n)): # n в цикле меняется а функции - revers_number(n) остается первое введенное.не разобрался почему.
        print(f'n = {n} , reverse = {revers_number(n)}')
        n += revers_number(n)
    print(n)
polindrom_namber(N)
