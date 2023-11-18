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


    def show(self):
        super().show()
        print(self.std)

class seventh(school):
    def __init__(self,name,roll_no,grade,sec):
        super().__init__(name,roll_no,grade)
        self.sec = sec


    def show(self):
        super().show()
        print(self.sec)


s1 = seventh('selva',24,10,5)
s1.show()
s2 = sixth('siva',24,'c','x')
s2.show()
