#Arithmetic Operators
print('-----------------------arithmetic operators---------------------------------')
x = 15
y = 4
print(x + y) #pertambahan
print(x - y) #pengurangan
print(x * y) #perkalian
print(x / y) #pembagian
print(x % y) #modulus
print(x ** y) #eksponensial
print(x // y) #floor division

#Assignment Operators
print('-----------------------assignment operators---------------------------------')
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

#Python Comparison Operators
print('-----------------------comparison operators---------------------------------')
x = 5
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

x = 5
print(1 < x < 10)
print(1 < x and x < 10)

#Python Logical operators
print('-----------------------logical operators---------------------------------')
#and
x = 5
print(x > 0 and x < 10)

#or
x = 5
print(x < 5 or x > 10)

#not
x = 5
print(not(x > 3 and x < 10))




