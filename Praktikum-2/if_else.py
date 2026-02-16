#if statement
print('-----------------------if statement---------------------------------')
a = 33
b = 200
if b > a:
  print("b is greater than a")

number = 15
if number > 0:
  print("The number is positive")

#Multiple Statements in If Block
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

#Using Variables in Conditions
is_logged_in = True
if is_logged_in:
  print("Welcome back!")

#elif statement
print('-----------------------elif statement---------------------------------')
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#Multiple Elif Statements
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

#Kategori umur
age = 25
if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")

#Day of the week checker
day = 3
if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")

#Else statement
print('-----------------------else statement---------------------------------')
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#Else Without Elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Checking even or odd numbers
number = 7
if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

#Temperature classifier (Combine if-elif-else)
temperature = 22
if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")

#validating user input (Else as Fallback)
username = "Emil"
if len(username) > 0:
  print("Welcome, {username}!")
else:
  print("Error: Username cannot be empty")





