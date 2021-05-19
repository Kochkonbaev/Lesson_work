class Animals:
    name_1 = "Lion"
    name_2 = "Dog"
    name_3 = "Cat"
    name_4 = "Rats"

    def home(self):
        print("Домашние животные")
        pass

    def wild(self):
        print("Дикие животные")
        pass

ani_a = Animals()

print(ani_a.wild())
print(ani_a.name_1)
print(ani_a.name_4)

ani_b = Animals()

print(ani_b.home())
print(ani_b.name_2)
print(ani_b.name_3)
