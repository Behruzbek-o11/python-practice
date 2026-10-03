#Shopping receipt generator

def total(price1,price2,price3):
    total_price = round((price1 + price2 + price3), 1)
    return total_price

def discount_label(total_price):
    if total_price >= 100:
        label = "20% OFF"
    elif total_price >= 50:
        label = "10% OFF"
    else:
        label = "No discount"
    return label

def print_receipt(customer, free_shipping=75):
    p1 = float(input("Enter 1st item price: "))
    p2 = float(input("Enter 2nd item price: "))
    p3 = float(input("Enter 3rd item price: "))
    total_price = total(p1,p2,p3)
    discount = discount_label(total_price)
    if total_price >= free_shipping:
        status = "FREE"
    else:
        status = "PAID"
    print(f"Customer : {customer}")
    print(f"Prices   : [{p1}, {p2}, {p3}]")
    print(f"Total    : {total_price}")
    print(f"Discount : {discount}")
    print(f"Shipping : {status}")


print_receipt("Ali")
