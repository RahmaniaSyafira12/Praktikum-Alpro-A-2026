#python function
print('-----------------------python function---------------------------------')
#create and calling function
def my_function():
  print("Hello from a function")

my_function()
my_function()

#kode dpt digunakan kembali dgn function
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

#function yg mengembalikan nilai
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

#menggunakan nilai kembalian scr langsung
def get_greeting():
  return "Hello from a function"

print(get_greeting())

#python arguments
print('-----------------------python arguments---------------------------------')
#sebuah fungsi dg satu argumen
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

#nilai default parameter negara
def my_function(country = "Norway"):
  print("I am from", country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#argumen kata kunci
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
my_function(animal = "dog", name = "Buddy")

#argumen posisional
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
my_function("dog", "Buddy")

