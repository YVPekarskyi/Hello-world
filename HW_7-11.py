#7

american_date = ("11.27.1992")
month = american_date[:2]
day = american_date[3:5]
year = american_date[6:]
print("European`s format: %s.%s.%s" % (day, month, year))

#---------------------------------------------------------
#8

my_name = ("Yaroslav Pekarskyi")
name_split = my_name.split(" ")
name = name_split[0]
surname = name_split[1]
print("my name %s it's %s %s" % (my_name, surname, name))

#---------------------------------------------------------
#9

snake_style = ("winter_spring_summer_autumn")
weather = snake_style.split("_")
wint = weather[0].capitalize()
spr = weather[1].capitalize()
summ = weather[2].capitalize()
aut = weather[3].capitalize()
print("%s it`s %s%s%s%s" % (snake_style, wint, spr, summ, aut))

#----------------------------------------------------------
#10

writer = "Leo Tolstoy*1828-08-28*1910-11-20"
writer_split = writer.split('*')
name = writer_split[0]
birth_date = writer_split[1]
death_date = writer_split[2]
birth = birth_date.split("-")
death = death_date.split("-")
birth_year = birth[0]
death_year = death[0]
age = int(death_year) - int(birth_year)
print("Writer is %s, %d" % (name, age))

#----------------------------------------------------------
#11

import math

def degree_conv_radians(a, b, c):
    result_degree_conv_radians1 = (math.cos(a*math.pi / 180))
    result_degree_conv_radians2 = (math.cos(b*math.pi / 180))
    result_degree_conv_radians3 = (math.cos(c*math.pi / 180))
    return (result_degree_conv_radians1, result_degree_conv_radians2, result_degree_conv_radians3)

cos1, cos2, cos3 = degree_conv_radians(40, 45, 60)
result = ("cos 40 = %.2f, cos 45 = %.2f, cos 60 = %.2f" % (cos1, cos2, cos3))
print (result)






















