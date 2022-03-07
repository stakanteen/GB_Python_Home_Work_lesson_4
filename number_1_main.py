#1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import sys
from home_work_lesson_4 import number_1_salary

try:
    way, work_time, salary_per_hour, reward = sys.argv
except ValueError:
    print('Invalid_args')
    exit()

print('Ваша зарплата: ', number_1_salary.salary(float(work_time), float(salary_per_hour), float(reward)))