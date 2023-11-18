class school:
    def __init__(self,name,age,roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

    def show(self):
        print(self.name)
        print(self.age)
        print(self.roll_no)

class nursery(school):
     def __init__(self,name,age,roll_no):
         #school.__init__(self,name,age,roll_no)
                #or
         # self.name = name
         # self.age = age
         # self.roll_no = roll_no
                #or
         super().__init__(name,age,roll_no)
class high(school):
    def __init__(self, name, age, roll_no):
        school.__init__(self, name, age, roll_no)

s1 = school('kumar',15,'12')
s2 = nursery('sam',6,10)
s3 = high('kevin',30,11.10)
s1.show()
s2.show()
s3.show()