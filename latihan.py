#list
thislist = [75, 80, 65, 90, 85]
thislist.append(95)
print(thislist)
thislist.remove(65)
print(thislist)
thislist.sort()
print(thislist)
print("nilai tertinggi:", thislist[-1])
print("nilai terendah:", thislist[0])

#Tuple
thistuple = ["D001", "Dr. Andi", "Struktur Data", 12]
print(thistuple[1]) #nama dosen
print(thistuple[2]) #mata kuliah yg diampu
for x in thistuple:
    print(x)

y = list(thistuple)
y[3] = 14
thistuple = tuple(y)
print(thistuple) 
#kelebihan tuple dibandingkan list adalah tuple lebih simple

#set
keahlian_A = {"Python","Java", "SQL", "Git"}
keahlian_B = {"Python", "C++", "Git", "Docker"}
myset = keahlian_A.intersection(keahlian_B) #keahlian A&B
print(myset)
set3 = keahlian_A.difference(keahlian_B)
print(set3) #keahlian hanya A
set4 = keahlian_B.difference(keahlian_A)
print(set4) #keahlian hanya B




