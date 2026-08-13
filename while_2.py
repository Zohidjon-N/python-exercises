#e-market

choice=int(input(f"Do you want to buy or sell?\n"
             f"Enter 0 for buying....\n"
             f"Enter 1 for selling...\n"))

products = {
    "Laptop": 850,
    "Smartphone": 600,
    "Headphones": 50,
    "Mouse": 25,
    "Keyboard": 40
}
if choice == 0:
    while True:
        name_product = input(f"Enter the product name"
              f"(or enter 'exit' to stop) ").title()
        if name_product == 'Exit':
            print('Thank you!')
            break
        elif name_product in products:
            print(f"Cost of {name_product} is ${products[name_product]}")
        else:
            print(f"Unfortunately, there's no {name_product}!")
elif choice == 1:
    while True:
        new_product = input(f"Enter the product name"
              f"(or enter 'exit' to stop) ").title()  
    
        if new_product == 'Exit':
            print('Thank you!')
            break
        
        cost_product = input(f"Enter the product cost"
                      f"(or enter 'exit' to stop) ").title()
        if cost_product == 'Exit':
            print('Thank you!')
            break
        else:
            products[new_product] = int(cost_product)    


    