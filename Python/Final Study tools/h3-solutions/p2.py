# Python Programming.
# Homework 3, problem 2
# Instructor: Dr. Ionut Cardei
# Do not distribute.


class Product:
    def __init__(self, name:str, mass:float=0, stock:int=0, price:float=0):
        self._name = name
        self._mass = mass
        self._stock = stock
        self._price = price

    def name(self):
        return self._name

    def mass(self):
        return self._mass

    def stock(self):
        return self._stock

    def price(self):
        return self._price

    def set_price(self, price):
        self._price = price        

    def __str__(self):
        return "{}, ${}, {} kg, {} in stock".format(self.name(), self.price(), self.mass(), self.stock())


class DiscountedProduct(Product):
    def __init__(self, discount:float, product:Product):
        self._product = product
        self._discount = discount


    def price(self):
        return (1.0 - self._discount) * self._product.price()


    def __str__(self):
        return "discounted {0:.2%}: {1}, ${2}, {3} kg, {4} in stock".format(self._discount,
                 self._product.name(), self.price(), self._product.mass(), self._product.stock())



def main():
    # create a product object for Lavalamps, priced at $100, and with 123 of them in stock:
    p = Product(name="Lavalamp", price=30, mass=0.8, stock=123)
    print(p)
    # prints "Lavalamp, $30, 0.8 kg, 123 in stock"
    # p.price() returns 30.0
    # create a discounted product of p, with a 20% discount:
    disc_p = DiscountedProduct(0.2, p)
    print(disc_p.price()) # prints "24" (24 == 30 - 20% * 30)
    print(disc_p)
    # prints "discounted 20%: Lavalamp, $24, 0.8 kg, 123 in stock"
    # now, we change the product p:
    p.set_price(20)
    print(p.price())
    # prints "20"
    # the price change also affects the discounted product object that embeds p:
    print(disc_p) # prints "discounted 20%: Lavalamp, $16, 0.8 kg, 123 in stock"
    # disc_p.price() returns 16 (16 == 20 - 20% * 20)
    
if __name__ == "__main__":
    main()
     


    
