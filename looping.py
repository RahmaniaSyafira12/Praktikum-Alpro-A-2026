#while loops
print('------------------------------while loop---------------------------------------')
#Print i as long as i is less than 6:
i = 1
while i < 6:
  print(i)
  i += 1
print('stop')

#Exit the loop when i is 3:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
print('stop')

#Continue to the next iteration if i is 3:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#for loop
print('-------------------------------for loop------------------------------------')
#Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
print('stop')

#Loop through the letters in the word "banana":
for x in "banana":
  print(x)
print('stop')

#Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
print('stop')

#Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
print('stop')

#do not print banana
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
print('stop')

print('range function')
#range() function
for x in range(6):
  print(x)
print('stop')

#menggunakan parameter awal
for x in range(2, 6):
  print(x)
print('stop')

#menambahkan angka 3 pada urutan
for x in range(2, 30, 3):
  print(x)
print('stop')

#else in for loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")
print('stop')

#Hentikan perulangan saat xnilainya 3
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
print('stop')

#peluang bersarang
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj: 
  for y in fruits:
    print(x, y)
print('stop')

#pass statement
for x in [0, 1, 2]:
  pass