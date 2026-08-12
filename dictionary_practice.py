# #create ductionary that describes someone

# my_idol={
#     'name':'Keonho',
#     'date_of_birth': 2009,
#     'group':'CORTIS',
#     'fav_music':'JoyRide'
# }

# print(f"My favourite idol is {my_idol['name']}."
#       f"He was born in {my_idol['date_of_birth']}y."
#       f" He is a member of K-POP group, {my_idol['group']}"
#       f" and his favourite song is {my_idol['fav_music']}.\n")

# #info about fav dish

# fav_dish={'Arya':'burger','Joh':'pizza','Niko':'hot-dog'}

# for name in fav_dish:
#     print(f"{name}'s favourite dish is {fav_dish[name]}.")
# print('\n')
# #Python dictionary

# python_terms = {
#     'variable': "o'zgaruvchi - ma'lumotlarni saqlash uchun xotiradagi idish",
#     'function': "funksiya - ma'lum bir vazifani bajaruvchi kodlar bloki",
#     'loop': "sikl - kodlarni bir necha marta takrorlash uchun ishlatiladi",
#     'dictionary': "lug'at - ma'lumotlarni kalit-qiymat (key-value) ko'rinishida saqlaydigan tuzilma",
#     'string': "matn - qo'shtirnoq ichiga olingan belgilar ketma-ketligi",
# }


# get_term=input('Enter the term to find its meaning>>> ')
# term=python_terms.get(get_term.lower(),'There is not term like that')
# print(f"{get_term.title()}, {term}")


#I'm waiter

menu = {
    # Appetizers & Starters
    "Caesar Salad": 8.50,
    "Tomato Soup": 6.00,
    "Garlic Bread": 4.50,
    
    # Main Courses
    "Grilled Chicken Breast": 14.99,
    "Cheeseburger with Fries": 12.00,
    "Beef Steak": 24.50,
    "Margherita Pizza": 11.50,
    "Creamy Alfredo Pasta": 13.25,
    
    # Desserts
    "Chocolate Cheesecake": 6.50,
    "Tiramisu": 7.00,
    "Vanilla Ice Cream": 4.00,
    
    # Beverages
    "Fresh Lemonade": 3.50,
    "Cappuccino": 4.00,
    "Bottled Water": 2.00
}

order=[]
no_order=[]

for _ in range(3):
    order.append(input(f"What do you want for {_+1}-dish? ").title())

for dish in order:
    if dish in menu:
        print(f"The cost of {dish} is ${menu[dish]}")
    else:
        no_order.append(dish)

for dish in no_order:
    print(f"Sorry, we have not {dish}")        

