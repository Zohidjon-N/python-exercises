#version 1
def find_fibonacci(n):
    first_num=1
    second_num=1
    print(first_num, end=" ")
    print(second_num, end=" ")
    for _ in range(n-2):
        temp=first_num
        first_num=second_num
        second_num=temp + second_num
        print(second_num, end=" ")

find_fibonacci(int(input('How many fibonacci numbers do you need? ')))        

#version 2

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
count = int(input('How many fibonacci numbers do you need? '))
fib_list=[]
for i in range(1,count+1):
    fib_list.append(fibonacci(i))

print(fib_list)    




