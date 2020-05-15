var_inc = int(input("Выручка компании:\n"))
var_exp = int(input("Издержки компании:\n"))
var_rev = var_inc - var_exp
print('Прибыль составила: ', "{:.3f}".format(var_rev))
while var_rev > 0:
    var_mar = var_rev / var_inc
    print('Рентабельность: ', "{:.3f}".format(var_mar))
    var_num = int(input('Введите число сотрудников:\n'))
    d = var_rev / var_num
    print('Прибыль на одного сотрудника составила:', "{:.3f}".format(d))
    break
print('Программа завершена')