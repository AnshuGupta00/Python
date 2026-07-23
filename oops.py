class Dog:
    species = "Huskey"  

    def __new__(this, name, age):
        this.name = name
        this.age = age


print(Dog.species)
print(Dog("Tommy", 5).name)