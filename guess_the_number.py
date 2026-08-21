from random import randint
while True:
    number = randint(1,10)

    print('Let\'s play number guessing game!')
    print('I\'ve thought number between 1 and 10. Guess what number I\'ve thought.')

    guess = int(input('>>> '))
    count=1
    while number!=guess:
        if guess > number:
            print('Incorrect, it\'s smaller. Try again')
            guess = int(input('>>> '))
        else:
            print("Incorrect, it's bigger")
            guess = int(input('>>> '))
        count+=1  
    print(f"Congratulations, you've found it in {count} attempt!")   

    print("Now think of a number between 1 and 10. I will try to find it.")
    input("If you've thought of it, press any key to continue...")

    thought= randint(1,10)
    count2 = 1
    low , high = 1, 10
    while  True:
        print(f"The number you've thought is {thought}: true(T), the number I've thought is bigger(+), smaller(-)")
        answer= input(">>> ")
        if answer.title() == 'T':
            if count> count2:
                print(f"I win! You've found the number with {count} guess, I've found it with {count2}")
            elif count<count2:
                print(f"You win! You've found the number with {count} guess, I've found it with {count2}")
            else:
                print(f"It's tie! We've both found the number with {count} guess.")        
            break
        elif answer == '-':
            high = thought
            thought=randint(low, high-1)
        elif answer == '+':
            low = thought
            thought = randint(low+1, high)
        else:
            print('Unsupported symble. Try again!')
            answer= input(">>> ") 
        count2+=1

    choice = input('Do you want play again(yes/no)')
    if choice == "no":
        break


