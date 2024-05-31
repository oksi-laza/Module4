from Module4.module_4_1.fake_math import divide as f_div
from true_math import divide as t_div


res1 = f_div(18, 3)
res2 = f_div(18, 0)
res3 = t_div(25, 5)
res4 = t_div(25, 0)
print(f'Результат деления: {res1}')
print(f'Результат деления: {res2}')
print(f'Результат деления: {res3}')
print(f'Результат деления: {res4}')