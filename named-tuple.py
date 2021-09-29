import collections, pprint

Sale = collections.namedtuple("Sale",
    "productid customerid date quantity price")
sales = []

with open("day4/sales.txt") as file:
    lines = file.readlines()
    for line in lines:
        list_values = line.strip().split()
        #tuple_values = tuple(list_values)
        sales.append(Sale(list_values[0], list_values[1], list_values[2], int(list_values[3]), float(list_values[4])))
        #sales.append(Sale(*list_values))


#sales.append(Sale(432, 921, "2010-12-14", 3, 7.99))
sales.append(Sale(419, 874, "2010-12-15", 1, 18.49))

pprint.pprint(sales)

total = 0
for sale in sales:
    if sale.productid != '432':
        continue
    total += sale.quantity * sale.price


#print("Total ${0}".format(total))
print("Total ${0:.4f}".format(total))
print("Total ${0:20.4f}".format(total))
