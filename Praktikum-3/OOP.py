#Classes/object

print('================================Classes/object==================================')

class MyClass: #ini kelas bernamaMyClass dengan properti bernama x
  x = 5

#Membuat beberapa object
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

#Hapus object
del p1

#class tanpa konten
class Person:
  pass

#__init__()method

print('==============================__init__()method====================================')

class Person:
  def __init__(self, name, age):  #metode __init__() digunakan untuk-
    self.name = name              #menetapkan nilai untuk nama dan usia, 
    self.age = age                #parameter dapat dimasukkan sebanyak yg diinginkan

#pembuatan object
p1 = Person("Emil", 36)

#pemanggilan object
print(p1.name)
print(p1.age)

#__init__()method dapat mengatur nilai default
class Person:
  def __init__(self, name, age=18): 
    self.name = name
    self.age = age

p1 = Person("Emil") #nilai default age=18
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)

#Self parameter

print('==============================Self parameter====================================')

#Digunakan self untuk mengakses properti kelas:
class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()

#Memanggil method dengan self
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):    #method (didefinisikan di dalam class)
    return "Hello, " + self.name #return greeting message
    
  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our website.")

p1 = Person("Tobias") #object (harus di luar class)
p1.welcome()          #pemanggilan method lewat object (harus di luar class)

#Properti kelas

print('==============================Properti kelas====================================')
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand) #mengakses property
print(car1.model)

#modify property
car1.brand = "tesla"   
print(car1.brand)

#add property
class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tony")

p1.age = 25
p1.city = "bekasi"

print(p1.name)
print(p1.age)
print(p1.city)

#Class property vs Object property/instance property
class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Object property (inner property)

p1 = Person("Eko")
p2 = Person("Tony")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

print('==============================Class method====================================')

#method dalam class
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet()

#method dengan parameter
class Calculator:       #bikin object dari class
  def add(self, a, b):  #a dan b parameter formal di method add
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))       #memanggil method add, output:8
print(calc.multiply(4, 7))  #memanggil method multiply, output:28

#method access object properties
class Person:
  def __init__(self, name, age):
    self.name = name   #atribut instance
    self.age = age     #atribut instance

  def get_info(self):
    return f"{self.name} is {self.age} years old"  #akses atribut object

p1 = Person("Tobias", 28)
print(p1.get_info())

#method untuk modifikasi properti suatu objek
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()
p1.celebrate_birthday()

#metode __str__()
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)

#class method dgn berbagai metode
class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()
