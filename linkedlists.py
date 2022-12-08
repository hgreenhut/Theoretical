class linkedLists:
    def __init__(self, value, pointer):
        self.value = value
        self.pointer = pointer
    def __str__(self):
        strr = ""
        strr += str(self.value)
        if (self.pointer != None):
            print(self.pointer)
        else:
            return strr
    def append(self, value):
        if self.pointer == None:
            self.pointer = value
        else:
            self.pointer.append(self, value)

        

b = linkedLists(8, 9)
a = linkedLists(4, b)
print(a)
a.append(7)


    
print(a)

