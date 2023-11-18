class school:  #class-keyword
    def __init__(self,name,age,grade):     #__init__ is called when an obj is created, it is a special methods, self-s1
        self.name = name  #self.name-attribute
        self.age = age
        self.grade = grade


s1 = school('vicky',15,7)  #constructor,s1-object
s2 = school('kumar',15,5)
teacher = school('ranjith',38,3)
print(s1.name)
print(s1.grade)
print(s2.age)
print(teacher.grade)
print(teacher.name)
print(type(teacher.name))
print(type(s2.age))

class book:
    org = 'ABC Pvt'                             #class attribute

    def __init__(self,title,author,price):      #obj/instance attribute
        self.title = title                      #b1.title
        self.author = author
        self.price = price

    def show(self):                             #obj method
        print(self.title)                       #b1.title
        print(self.author)
        print(self.price)
        print(self.org)

    def change_title(self,title2):
        self.title = title2

    def discount_price(self):
        self.price = self.price-(self.price/100)*10

    @classmethod
    def change_org(cls,new_org):
        cls.org=new_org


    @staticmethod
    def company_details():
        print('chennai')
        print('since 1948')





s1 = book('maths','vicky',100)  #constructor
s2 = book('social','kennedy',200)
s1.show()
s2.show()

s2.change_title('science')
s1.change_title('python')
s1.show()
s2.show()

s1.discount_price()
s1.show()
s2.discount_price()
s2.show()

s1.change_org('xyz pvt')
s1.show()
book.change_org('dbs pvt')
book.show()

book.company_details()
s1.company_details()
