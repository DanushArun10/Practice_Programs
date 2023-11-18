from abc import ABC,abstractmethod    #Abstract Base Class
class school(ABC):
    school_name = 'ABC school'
    def __init__(self,name,roll_no,grade):
        self.name = name
        self.roll_no = roll_no
        self.grade = grade

    @abstractmethod
    def s1(self):
        pass

    def show(self):
        print(self.name)
        print(self.roll_no)
        print(self.grade)
class sixth(school):
    def __init__(self,name,roll_no,grade,std):
        super().__init__(name,roll_no,grade)
        self.std = std

    def s1(self):
        print('child class',self.school_name)

    def show(self):
        super().show()
        print(self.std)


s2 = sixth('siva',24,'c','x')
s2.show()
