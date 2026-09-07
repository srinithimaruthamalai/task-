#condition
#1.  smallest number among two given integers
a=int(input("enter a a:"))
b=int(input("enter a b:"))
if a<b:
  print("smaller is a:",a )
else:
  print("smaller is b:",b )
#2. smallest number among two given integers
a=int(input("enter a a :"))
b=int(input("enter a b :"))
if a>b:
   print("larger is a:",a)
else:
   print("larger is b:",b)

#3. the absolute value of a given integer
num=int(input("enter a number:"))
if num<0:
  num=-num
  print("Absolute value is:", num)

#4. Check if a given number is even number or odd number
num=int(input("enter a number:"))
if num%2==0:
    print("number is even")
else:
    print("number is odd")
#5. the given number is a multiple of 5 or not
num=int(input("enter a number:"))
if num%5==0:
   print("the number is a  multiple of 5")
else:
    print("the number is not a multiple of 5")
    
#6. the given number is a multiple of 10 or not
num=int(input("enter a number:"))
if num%10==0:
   print("the number is a  multiple of 10")
else:
    print("the number is not a multiple of 10")

#7. Check whether the given number is a two-digit number or not.
num=int(input("enter a number:"))
if 10<= num <=99:
  print("the number is a two digit")
else:
  print("the number is not a two digit")

#8. Check whether the given number is a three-digit number or not.
num=int(input("enter a number:"))
if 100<= num <=999:
  print("the number is a three digit")
else:
  print("the number is not a three digit")

#9. Check if a given number ends with zero or not.
num=int(input("enter a number:"))
if num%10==0:
  print("The number ends with zero")
else:
  print("The number does not end with zero")

#10. Write a program to accept a number and check if its square is above 50 or below 50.
num=int(input("enter a number:"))
square=num**2
if square>50:
   print("Square is above 50")
else:
    print("Square is below 50")

#11.Write a program to accept two numbers, subtract the two numbers and check if the difference (answer) is 0 or not
num1=int(input("enter a num1:"))
num2=int(input("enter a num2:"))
difference=num1-num2
if difference==0:
  print("The answer is zero")
else:
  print("The anwser is not a zero")

#12.	Write a program to read the Computer Science marks of a student and print if the student has passed or failed. The student has passed if marks is 50 or above otherwise failed).
mark=int(input("enter a mark:"))
if mark>=50:
  print("pass mark")
else:
  print("fail mark")

#13.Write a program to accept a number and check if the number is divisible by 10.
num=int(input("enter a number:"))
if num%10==0:
  print("the number is divisible by 10")
else:
  print("the number is not divisible by 10")

#14.Write a program to take a two-digit number and print the biggest digit.
num =int(input("enter a two-digit number:"))
digit1 =num//10
digit2 =num%10
if digit1>digit2:
  print("biggest number is",digit1)
else:
  print("biggest number is", digit2)

#15. Write a program to accept the choice from the user. If the choice is 1 print “The exam will be easy”, otherwise print “The exam will be difficult”.
choice =int(input("enter youre choice:"))
if choice==1:
  print("The exam will be easy")
else:
  print("The exam will be difficult")

#16.Write a program to accept a value from the user. If the value entered is 1 then print “You can go out and play” otherwise “You cannot go out and play”
value =int(input("Enter a value:"))
if value==1:
  print("You can go out and play")
else:
  print("You cannot go out and play")
  
#17.Write a program to accept the length and breadth of a shape and print if they are the same. If they are the same, print it’s a square otherwise its rectangle.
length =int(input("Enter a length:"))
breadth =int(input("Enter a breadth:"))
if length== breadth:
  print("its square")
else:
  print("its rectangle")
  
#range:
| Character | ASCII Range |
| --------- | ----------: |
| `A–Z`     |       65–90 |
| `a–z`     |      97–122 |                              
| `0–9`     |       48–57 |

#18.Check if a given number is the ASCII value of an uppercase alphabet or not.
num =int(input("enter a number:"))
if num >= 65 and num <= 90:
  print("it is the ASCII valuse of an uppercase alphabet")
else:
  print("it is not the ASCII valuse of an uppercase alphabet")

#19.Check if a given number is the ASCII value of a lowercase alphabet.
num =int(input("enter a number:"))
if num >= 97 and num <= 122:
  print("it is the ASCII valuse of an lowcase alphabet")
else:
  print("it is not the ASCII valuse of an lowercase alphabet")

#20.Check if a given number is the ASCII value of a numeric character or not.
num =int(input("enter a number:"))
if num >= 48 and num <= 57:
  print("it is the ASCII valuse of an number character")
else:
  print("it is not the ASCII valuse of an number character")

#21.Check whether the given number is a multiple of both 5 and 3.
num =int(input("enter a number:"))
if num%5==0  and num%3==0:
  print("it is multiple of both 5 and 3")
else:
  print("it is not multiple of both 5 and 3")
  
#22. Check if a given number is a three-digit number and also a multiple of 10.
num =int(input("enter a number:"))
if num >= 100 and num <= 999 and num%10==0:
  print("it is multiple of 10")
else:
  print("it is not multiple of 10")
  
#23.Check if a given number is a three-digit number and also a multiple of 2, 5, and 10.
num =int(input("enter a number:"))
if num>= 100 and num<=  999 and num%2==0 and num%5==0 and num%10==0:
  print("it is multiple of both 2,5 and 10")
else:
  print("it is not multiple of both 2, 5 and 10")

#24.Check the given two integer inputs. If both numbers are even, find their product. Otherwise, find their sum.
num1 =int(input("enter a num1:"))
num2 =int(input("enter a num2:"))
if num1%2==0 and num2%2==0:
  product=num1*num2
  print("product=", product)
else:
  sum=num1+num2
  print("sum", sum)
  
Example:

1007 → ends with 7 → Buzz Number
21 → divisible by 7 → Buzz Number
25 → neither → Not a Buzz Number

#25.A number is said to be Buzz Number if it ends with 7 or is divisible by 7. Example: 1007 is a Buzz Number. Define a class Buzz number to read a number and check if it is a Buzz number or not.
num=int(input("enter a number:"))
if num%10==7 and  num%7==0:
  print("it is a buzz number")
else:
  print("it is not a buzz number")

#if elif else :

#1.Find the largest number among three integers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 >num2 and num1 >num3:
  print("largest number is",num1)
elif num2>num1 and num2>num3:
  print("largest number is",num2)
else: 
  print("largest number is",num3)

#2.Find the smallest number among three integers.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 <num2 and num1 <num3:
  print("largest number is",num1)
elif num2<num1 and num2<num3:
  print("smallest number is",num2)
else: 
  print("smallest number is",num3)

#3.Check if a given number is greater than 0, if yes then print 'Positive'. If the given
num=int(input("enter a number:"))
if num>0:
  print("postivie")
elif num<0:
  print("negative")
else :
  print("zero")

#4. A library charges fine for books returned late. To calculate the fine, define a class Library with the following .To input the number of days books were returned late. To calculate and print the fine based on the following condition:
days = int(input("Enter number of days late: "))

if days <= 5:
    fine = days * 0.40
elif days <= 10:
    fine = days * 0.65
else:
    fine = days * 0.80

print("Fine = Rs.", fine)

#5.Write a Python program that functions as a basic calculator. The program will prompt the user to input two numbers and a mathematical operation (+, -, x, /). It will then perform the selected operation and display the result on the screen.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Enter operation (+, -, x, /): ")

if operation == "+":
    result = num1 + num2
    print("Result =", result)

elif operation == "-":
    result = num1 - num2
    print("Result =", result)

elif operation == "x":
    result = num1 * num2
    print("Result =", result)

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result =", result)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid operation")

#6. Check whether the given number is a multiple of 5, 3, and 7.

num = int(input("Enter a number: "))

if num % 5 == 0 and num % 3 == 0 and num % 7 == 0:
    print("The number is a multiple of 5, 3, and 7")
else:
    print("The number is not a multiple of 5, 3, and 7")
#7. To input weight of the parcel and type of booking (`O' for ordinary and 'E' for express).To compute and display the charges based on the weight of the parcel as per the tariff given 
 
weight = int(input("Enter weight of parcel in grams: "))
booking = input("Enter type of booking (O for Ordinary, E for Express): ")

if weight <= 100:
    if booking == 'O':
        charge = 80
    else:
        charge = 100

elif weight <= 500:
    if booking == 'O':
        charge = 150
    else:
        charge = 200

elif weight <= 1000:
    if booking == 'O':
        charge = 210
    else:
        charge = 250

else:
    if booking == 'O':
        charge = 250
    else:
        charge = 300

print("Parcel Charge = ₹", charge)

#8. Write a program to compute the discount according to the given conditions for the purchase of laptop. to take the price of the laptop.to calculate the charge according to the following condition.
#Display the output as per the given format:
#Price of laptop : 
#Discount : 
#Total Price :
  
price = float(input("Enter the price of laptop: "))

if price <= 50000:
    discount = 0

elif price <= 100000:
    discount = price * 10 / 100

elif price <= 150000:
    discount = price * 15 / 100

else:
    discount = price * 20 / 100

total_price = price - discount

print("Price of laptop :", price)
print("Discount        :", discount)
print("Total Price     :", total_price)









