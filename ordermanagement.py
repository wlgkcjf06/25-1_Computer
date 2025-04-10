def getprice(p, q):
    return p * q

def apply_discount(p, r=0.1):
    return p * (1-r)

def add_order(o, n, a):
    o[n] = a

def printsummary (o):
    print ('\nOrder Summary:')
    for key in o:
        print(f"{key}: €${o[key]:.2f}")

def main():
    print('Welcome to the Order Management System!')
    print("Type 'exit' as the customer name to finish.\n")
    orders = {}
    while 1:
        name = input("Enter customer name (or type 'exit' to finish): ")
        if name.lower() == 'exit':
            break
        price = float(input('Enter item price: '))
        quantity = int(input('Enter quantity: '))
        discount = input("Apply discount? (yes/no): ").lower()

        if discount == 'yes':
            drate = float(input("Enter discount rate (e.g. 0.2 for 20%):"))
            bprice = getprice(price,quantity)
            tot = apply_discount(bprice, drate)
        else:
            tot = getprice(price,quantity)
        add_order(orders, name, tot)
        print(f'Order added for {name}. Total: €${tot:.2f}\n')
    printsummary(orders)

main()