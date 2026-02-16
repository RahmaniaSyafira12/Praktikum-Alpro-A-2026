class Hero:
  def __init__(self, nama, role, aksi): #atribut
    self.nama= nama
    self.role = role
    self.aksi = aksi

  #method attack
  def attack(self):
    print(f'{self.nama} menyerang dengan skill {self.aksi}!')
    
  #method info
  def info(self):
    print(f"Hero: {self.nama}, Role: {self.role}, Skill: {self.aksi}")

#bikin hero
p1 = Hero("Miya","marksman","menembakkan panah")
p2 = Hero("Vale","mage","melempar bola api")
p3 = Hero("Jonshon","tank","menabrak musuh")

heroes = [p1, p2, p3]

for hero in heroes:
    hero.info()
    hero.attack()

