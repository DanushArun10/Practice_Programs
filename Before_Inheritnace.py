class Book:
    org = 'ABC pvt'
    CEO = 'sam'

    def __init__(self, title, author, pages, price):
        self.title = title
        self.price = price
        self.author = author
        self.pages = pages

    def show(self):
        print(self.title)
        print(self.price)
        print(self.pages)
        print(self.author)

    def discount(self):
        self.price = self.price - (self.price *0.1)

class Magazine:
    org = 'ABC pvt'
    CEO = 'sam'

    def __init__(self, title, publisher, price, period):
        self.title = title
        self.price = price
        self.period = period
        self.publisher = publisher

    def show(self):
        print(self.title)
        print(self.price)
        print(self.period)
        print(self.publisher)

    def discount(self):
        self.price = self.price - (self.price *0.1)

class Newspaper:
    org = 'ABC pvt'
    CEO = 'sam'

    def __init__(self, title, publisher, price, period):
        self.title = title
        self.price = price
        self.period = period
        self.publisher = publisher

    def show(self):
        print(self.title)
        print(self.price)
        print(self.period)
        print(self.publisher)

    def discount(self):
        self.price = self.price - (self.price *0.1)


b1 = Book("wings of f", "Aldous Huxley", 311, 29.0)

n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")

m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

b1.show()
n1.show()
m1.show()




print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)