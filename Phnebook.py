import sys
def initial_phonebook():
    rows, cols = int(input("Please enter initial number of contacts: ")),5
    phonebook = []
    print(phonebook)
    for i in range(rows):
        print("\nEnter contact %d details in the following order (ONLY)" % (i + 1))
        print("NOTE : * indicates mandatory field")
        print("....................................................................................")
        temp = []
        for j in range(cols):
            if j == 0:
                temp.append(input("Enter Name* : "))
                if temp[j] == '' or temp[j] == ' ':
                        sys.exit("Name cannot be empty. Process terminated.")
            if j == 1:
                temp.append(input("Enter Number* : "))
                if temp[j] == '' or temp[j] == ' ':
                        sys.exit("Number cannot be empty. Process terminated.")
            if j == 2:
                temp.append(input("Enter Email address : "))
                if temp[j] == '' or temp[j] == ' ':
                        temp[j] = None
            if j == 3:
                temp.append(input("Enter Date of Birth : "))
                if temp[j] == '' or temp[j] == ' ':
                        temp[j] = None
            if j == 4:
                temp.append(input("Enter catagory(Family/Friends/Work/Others) : "))
                if temp[j] == '' or temp[j] == ' ':
                        temp[j] = None
        phonebook.append(temp)
    print(phonebook)
    return phonebook

def menu():
      print("***********************************************")
      print("\t\tSMARTPHONE DIRECTORY")
      print("***********************************************")
      print("\tYou can now perform the following operations on this phonebook\n")
      print("1. Add a new contact")
      print("2. Remove an existing contact")
      print("3. Delete all contact")
      print("4. Search for a contact")
      print("5. Display all contacts")
      print("6. Exit")

      choice = int(input("Please enter your choice: "))
      return choice
def add_contact(pb):
        temp = []
        for j in range(len(pb[0])):
            if j == 0:
                temp.append(input("Enter Name* : "))
                if temp[j] == '' or temp[j] == ' ':
                        sys.exit("Name cannot be empty. Process terminated.")
            if j == 1:
                temp.append(input("Enter Number* : "))
                if temp[j] == '' or temp[j] == ' ':
                        sys.exit("Number cannot be empty. Process terminated.")
            if j == 2:
                temp.append(input("Enter Email address : "))
                if temp[j] == '' or temp[j] == ' ':
                        temp[j] = None
            if j == 3:
                temp.append(input("Enter Date of Birth : "))
                if temp[j] == '' or temp[j] == ' ':
                        temp[j] = None
            if j == 4:
                temp.append(input("Enter catagory(Family/Friends/Work/Others) : "))
                if temp[j] == '' or temp[j] == ' ':
                        temp[j] = None
                                    
        pb.append(temp)
        return pb

