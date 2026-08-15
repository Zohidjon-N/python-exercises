info={}

def get_info(name,surname,date_birth, address, email='', phone=''):
    info={
        'name': name,
        'surname': surname, 
        'date_birth': date_birth, 
        'address': address, 
        'email': email,
        'phone': phone
        }

    return info

info_list=[]

while True:

    number = int(input('Phone number'))
    email = input('Email: ')
    address =input('Address: ')
    date_birth=int(input('Year of birth: '))
    surname=input('Surname: ')
    name=input('Name: ')

    info_list.append(get_info(name,surname,date_birth,address,email,number))

    if 'yes'==input('Do you want exit(yes/no)'):
        print('Thank you!')
        break