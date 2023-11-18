# Class and Object

class book:
    org_name = 'SB pvt'
    def __init__(self,name,author,price):
        self.name = name
        self.author = author
        self.price = price

    def show(self):
        print(self.name)
        print(self.author)
        print(self.price)

class magazine:
    def __init__(self,name,publisher,price):
        self.name = name
        self.publisher = publisher
        self.price = price

    def show(self):
        print(self.name)
        print(self.publisher)
        print(self.price)

class newspaper:
    def __init__(self,name,publication,price):
        self.name = name
        self.publication = publication
        self.price = price

    def show(self):
        print(self.name)
        print(self.publication)
        print(self.price)


c1 = newspaper('Fire','Sura',1500)
c1.show()
c2 = magazine('wings','mag',1300-500)
c2.show()