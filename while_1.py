
#cost of ticket
while True:
    age= input(f"Enter your age: "
               f"(enter 'exit' or 'stop')")

    if age == 'stop' or age == 'exit':
        print('Stop!')
        break 

    elif 0<int(age)<=7:
        print("Cost of ticket is $0.2")
    elif 7<int(age)<=18:
        print("Cost of ticket is $0.3") 
    elif 18<int(age)<=65:
        print("Cost of ticket is $1.0")
    elif int(age)>65:
        print("Ticket is free!")  
    else:
        print('Enter the age greater than 0')    