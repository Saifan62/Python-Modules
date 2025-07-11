print("Star Pattern \n")
for i in range (1,11):
    for j in range(i):
        print("*", end="")
    print('\n')

print("Inverted Star pattern \n")
for i in range (10,0,-1):
    for j in range(i,1,-1):
        print("*", end="")
    print('\n')

