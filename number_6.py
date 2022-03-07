# 6. Реализовать два небольших скрипта:

# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.

# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

# Part 1
from itertools import count, cycle

from_input_gen = int(input('Для генератора целых числе введите начальное целое число: '))
to_input_gen  = int(input('Для генератора целых числе введите конечное целое число: '))

def generator_int_in_range (from_, to_):
    for el in count(from_):
        if el > to_:
            break
        else:
            print(el)

generator_int_in_range(from_input_gen, to_input_gen)

# Part 2
list_input_cycle = list(input
                        ('Для цикличнского итератора введите список значенй, '
                         'который нужно повторять через пробел: ').split(sep=' ')
                        )
count_input_cycle  = int(input('Для цикличнского итератора укажите количество повторений: '))

def cycle_list_iteraror (input_list, count_cycle):
    сounter = 0
    end_cycle = len(input_list) * count_cycle - 1
    for el in cycle(input_list):
        if сounter > end_cycle:
            break
        print(el)
        сounter += 1

cycle_list_iteraror(list_input_cycle, count_input_cycle)
