inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

for element in inventory:
    ea_element = element.split(", ")
    item = ea_element[0]
    qty = ea_element[1]
    price = ea_element[2]
    print("The store has {} {}, each for {} USD.".format(qty, item, price))