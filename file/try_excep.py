# #task 1

# try:
#     num = int(input("Enter integer: "))
    

# except ValueError:
#     print("Please enter a valid integer.")
# else:
#     print("Square of the integer is:", num**2)    


#task 2
try:
    num1 = int(input("Enter two integers to find their devisons:"))
    num2 = int(input())
    result = num1/num2
except ZeroDivisionError:
    print('It\'s not allowed to divide by 0')
except ValueError:
    print('Please enter a valid integer')
else:
    print(f"{num1} : {num2} = {result}")
finally:
    print("Program is finished!")
        




