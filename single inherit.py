class school:
    def __init__(self,name,roll_no,grade):
        self.name = name
        self.roll_no = roll_no
        self.grade = grade

    def show(self):
        print(self.name)
        print(self.roll_no)
        print(self.grade)


class sixth(school):
    def __init__(self,name,roll_no,grade,std):
        super().__init__(name,roll_no,grade)
        self.std = std

    def show1(self):
        super().show()
        print(self.std)

s6 = sixth('kumar',12,'c','iv')
s6.show1()