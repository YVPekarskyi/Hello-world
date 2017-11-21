#13
# Написать функцию, которая будет проверять четность некоторого числа.

def even_number(number):
    if number % 2 == 0:
        print ('even number')

    else:
        print('not even number')

even_number(2873)

#14
#Пользователь вводит длины катетов прямоугольного треугольника.
#Написать функцию, которая вычислит площадь треугольника и его периметр. Результат работы функции вывести на печать.

import math
def square_and_perimeter_triangle(k1, k2):
    if k1 > 0 and k2 > 0:
        square_triangle = k1*k2 / 2
        hypotenuse_triangle = math.sqrt(k1**2 + k2**2)
        perimeter_triangle = hypotenuse_triangle + k1 + k2
        return(square_triangle, perimeter_triangle)

result1, result2 = square_and_perimeter_triangle(14, 6)
result3 = ("Площадь и периметр прямоугольного треугольника ровны "
           "%d кв.см и %d см соответственно" % (result1, result2))
print(result3)



