class Parrot:

 # Class variable
    species= "bird"
    def __init__(self,name,age):       
        self.name= name
        self.age= age
    def sing(self,song):
        return "{} sings {}".format(self.name, song)
    def dance(self):
        return "{} is now dancing".format(self.name)


# Object creation
blu=  Parrot("Blu",10)
woo= Parrot("Woo", 15)

# Accessing class variable
print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))
# Accessing instance variables
print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))

# Calling instance methods
print(blu.sing("Montagem bailao"))
print(blu.dance())
print(woo.sing("Montagem ladrao"))
print(woo.dance())