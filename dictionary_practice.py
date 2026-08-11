#create ductionary that describes someone

my_idol={
    'name':'Keonho',
    'date_of_birth': 2009,
    'group':'CORTIS',
    'fav_music':'JoyRide'
}

print(f"My favourite idol is {my_idol['name']}."
      f"He was born in {my_idol['date_of_birth']}y."
      f" He is a member of K-POP group, {my_idol['group']}"
      f" and his favourite song is {my_idol['fav_music']}.\n")

#info about fav dish

fav_dish={'Arya':'burger','Joh':'pizza','Niko':'hot-dog'}

for name in fav_dish:
    print(f"{name}'s favourite dish is {fav_dish[name]}.")
print('\n')
#Python dictionary

python_terms = {
    'variable': "o'zgaruvchi - ma'lumotlarni saqlash uchun xotiradagi idish",
    'function': "funksiya - ma'lum bir vazifani bajaruvchi kodlar bloki",
    'loop': "sikl - kodlarni bir necha marta takrorlash uchun ishlatiladi",
    'dictionary': "lug'at - ma'lumotlarni kalit-qiymat (key-value) ko'rinishida saqlaydigan tuzilma",
    'string': "matn - qo'shtirnoq ichiga olingan belgilar ketma-ketligi",
}


get_term=input('Enter the term to find its meaning>>> ')
term=python_terms.get(get_term.lower(),'There is not term like that')
print(f"{get_term.title()}, {term}")