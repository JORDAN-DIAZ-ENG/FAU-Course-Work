# Written by Jordan Diaz for python class midterm

def main():
    """ Main driver function"""
    sales_data = [('iPhone X', 10, 1000, 950), ('Samsung Galaxy X', 25, 970, 850), ('Google Pixel 2', 7, 650, 600)]

    # part a)
    sales_prod = [(sale[0], sale[1] * sale[2]) for sale in sales_data]
    print(sales_prod)

    # part b)
    total_profit = sum([(sale[1] * (sale[2] - sale[3])) for sale in sales_data])
    print(total_profit)


if __name__ == "__main__":
    main()
