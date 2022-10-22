# this program experiments with class inheritance
class Product(object):
    def __init__(self, name, mass=0.0, stock=0, price=0.0):
        """ Constructor"""
        self.product_name = name
        self.product_mass = float(mass)
        self.product_stock = stock
        self.product_price = float(price)

    def __str__(self):
        return "{}, ${}, {} kg, {} in stock".format(self.product_name, self.product_price, self.product_mass,
                                                    self.product_stock)

    def name(self):
        return self.product_name

    def mass(self):
        return self.product_mass

    def stock(self):
        return self.product_stock

    def price(self):
        return self.product_price

    def set_price(self, new_price):
        self.product_price = float(new_price)


class DiscountedProduct(Product):
    def __init__(self, discount, product):
        Product.__init__(self, product.product_name, product.product_mass, product.product_stock,
                         product.product_price - (discount * product.product_price))
        self.product_discount = discount
        self.base_product = product

    def __str__(self):
        """ prints out the data from the discounted product"""

        # refreshes the data
        self.__init__(self.product_discount, self.base_product)
        return "discounted {}%: {}, ${}, {} kg, {} in stock".format(self.product_discount * 100, self.product_name,
                                                                    self.product_price, self.product_mass,
                                                                    self.product_stock)


def main():
    """ Main function"""
    p = Product(name="Lava lamp", price=30, mass=0.8, stock=123)
    disc_p = DiscountedProduct(0.2, p)
    print(p)
    print(disc_p)
    p.set_price(20)
    print(p.price())
    print(disc_p)


if __name__ == "__main__":
    main()
