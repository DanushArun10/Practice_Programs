class school:
    def __init__(self,name,age,role):
        self.name = name
        self.age = age
        self.role = role

    def show(self):
        print(self.name)
        print(self.age)
        print(self.role)

class seventh(school):
    def __init__(self,name,age,role,roll_no):
        super().__init__(name,age,role)
        self.roll_no = roll_no

    def show1(self):
        super().show()
        print(self.roll_no)

class sixth(seventh):
    def __init__(self,name,age,role,roll_no,sec):
        super().__init__(name,age,role,roll_no)
        self.sec = sec

    def show2(self):
        super().show1()
        print(self.sec)


s1 = sixth('kumar',14,'student',13,'A')
s1.show2()

s1 = seventh('rakesh',15,'student',26)
s1.show1()
