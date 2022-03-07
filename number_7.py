#7. Реализовать генератор с помощью функции с ключевым словом yield,создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо
# выводить только первые n чисел, начиная с 1! и до n!.

# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

#Важно!
#При отправке домашнего задания обязательно нажимайте галочку "Показать задание ментору".

from math import factorial

input_integer_for_factorial = int(input('Укажите число факториала: '))
input_end_ = int(input('Укажите количество первых элементов для отображения: '))

def fact (integer_for_factorial):
    for int_ in range(1, integer_for_factorial+1):
        el = factorial(int_)
        yield el

counter = 1
for el in fact(input_integer_for_factorial):
    if counter > input_end_:
        break
    else:
        print(el)
    counter += 1