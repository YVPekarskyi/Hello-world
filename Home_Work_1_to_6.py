a = 15
b = 4
c = 120
formula = a + b*(c / 2)
result = "результат уравнения при a = %d, b = %d, с = %d равно %d" % (a, b, c, formula)
print (result)

#-----------------------------------------
a = 9
b = 18
formula = (a**2 + b**2)%2
result  = "результат уравнения при a = %d, b = %d равно %d" % (a, b, formula)
print (result)

#-----------------------------------------
a = 355
b = 76
c = 98
formula = (a + b) / 12*c % 4 + b
result = "результат уравнения при a = %d, b = %d, с = %d равно %d" % (a, b, c, formula)
print (result)

#-----------------------------------------
a = 8
b = 12
c = 2
formula = (a - b*c) / (a + b) % c
result = "результат уравнения при a = %d, b = %d, с = %d равно %.d" % (a, b, c, formula)
print (result)

#-----------------------------------------
import math
a = 4
b = -12
c = 1
formula = math.fabs(a - b) / math.pow((a + b), 3) - math.cos(c*math.pi / 180)
result = "результат уравнения при a = %d, b = %d, с = %d равно %.4f" % (a, b, c, formula)
print (result)

#------------------------------------------
a = 100
b = 5
c = 25
formula = math.pow((math.log(1 + c) / -b), 4) + math.fabs(a)
result = "результат уравнения при a = %d, b = %d, с = %d равно %.d" % (a, b, c, formula)
print (result)
