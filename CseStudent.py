class CSStudent:
    #Class variable
    stream= "CSE"
    # The init method
    def __init__(self,roll):
        self.roll= roll
        
    def set_address(self, address):
            self.address = address
    def get_address(self):
        return self.address
add = CSStudent(101)
add.set_address("123 Main St")
print(add.get_address())
print(CSStudent.stream)

        