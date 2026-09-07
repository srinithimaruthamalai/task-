#1.  Write a Program to Print Hello world!
print("Hello")
#2.  Write a Program to Add,Sub,Multiply,Divide,Modules of Two Numbers
a=20
b=10
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
#3. Write a Program to Find the Square Root [formula = number **0.5]
number  =100
square_root  =number**0.5
print("square root=",square_root)
#4. Write a Program to Calculate the Area of a Triangle [formula = 0.5 x base x height]
base =5
height =10
area=0.5*base*height
print("Area of the triangle=",area)
#5. Write a Program to Solve Quadratic Equation [ (a+b)2 formula , (a-b)2 formula ,a2-b2  formula ]
a=2
b=3
print("(a+b)^2=",(a+b)**2)
print("(a-b)^2=",(a-b)**2)
print("a^2-b^2=",a**2-b**2)
#6. Write a Program to Swap Two Variables  [using third variable , without using third variable]
a=2
b=3
temp=a
a=b
b=temp
print("After swapping:")
print("a=",a)
print("b=",b)
#without using variable
a=2
b=3
a,b=b,a
print("After swapping:")
print("a=",a)
print("b=",b)
#7. Write a Program to Convert Kilometers to Miles [ 1km = 0.63 miles ]
km=10
miles=km*0.63
print("miles=",miles)
#8. Write a Program to Convert Celsius To Fahrenheit [ formula = (Celsius x 1.8) + 32]
celsius=100
fahrenheit=(celsius*1.8)+32
print("fahrenheit=",fahrenheit)
#9. Write a program to find last digit of the number
number  =25
last_digit=number%10
print("last digit=",last_digit)
#10.Write a program to find last two digit of the number
number  =135
last_two=number%100
print("last digit=",last_two)
#11.Write a program to take a five-digit number as input, square the middle digit and print number and the square.
number=54623
middle_digit=(number//100)%10
square=middle_digit**2
print("number=",number)
print("middle digit=",middle_digit)
print("square=",square)
