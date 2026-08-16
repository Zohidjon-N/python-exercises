
def find_prime(a, b=0):
    prime_list=[]
    while b<=a:
        count=0
        for number in range(2,int(b**(0.5))+1):
            if b%number==0:
                count+=1
        if count==0:
            prime_list.append(b)
        b+=1
    return prime_list    

num1=int(input('Enter first number of interval>>> '))   
num2=int(input('Second number>>> '))    

number=find_prime(num2,num1)
print(number)

    




