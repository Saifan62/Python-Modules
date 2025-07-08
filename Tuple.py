my_tuple=()
print(my_tuple)

my_tuple=(1,2,3)
print(my_tuple)

my_tuple=(1, "Hello", 3.4, True)
print(my_tuple)

my_tuple=('m','i','n','e','c','r','a','f','t')
print(my_tuple[4])

n_tuple=("logitech", [8,4,6], (1,2,3))
print(n_tuple[0][3])
print(n_tuple[1][1])
print("Slicing the tuple:", n_tuple[1][0:2])
for letter in(my_tuple):
    print("Hello", letter)