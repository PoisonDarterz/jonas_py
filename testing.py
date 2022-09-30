
import platform
from math import pi

print(platform.python_version())

print('Hello World!')

#4
r = float(input("Input radius of circle: "))
area = pi * r * r
print("The area of circle is: ", area, "\n")

#5
firstname = input("Input first name: ")
lastname = input("Input last name: ")
print(lastname, " ", firstname)

#6
q6 = input("Input comma seperated integers (without spaces): ")
q6list= q6.split(",")
q6tuple = tuple(q6list)
print (q6list, "\t" , q6tuple , "\n")

#8
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0] , " " , color_list[-1] , "\n")

#16
q16 = int(input("Input an integer: "))
if q16 < 17 :
    diff = 17 - q16
else:
    diff = q16 - 17
print ("The difference is: " , diff , "\n")

#18
q18 = [int(input("Input a number: ")) for x in range(3)]
freq = sum = 0
for y in range(2):
    if(q18[y] == q18[y+1]):
        freq = freq+1
for z in range(3):
    sum = sum + q18[z]
if(freq==2):
    print (3 * sum)
else:
    print (sum)