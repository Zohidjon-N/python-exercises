import json
#task1
data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}

json_data = json.dumps(data)
print(json_data)
print(type(json_data))

#task2
talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}""" 

talaba = json.loads(talaba_json)
print(f"{talaba['ism']} {talaba['familiya']}") 

#task3
with open('data.json','w') as file:
    json.dump(json_data, file)

with open('talaba.json','w') as file:
    json.dump(talaba_json,file)

#task4
with open('students.json') as file:
    students_dic = json.load(file)
print(type(students_dic))
print(students_dic)

for person in students_dic['student']:
    print(f"{person['name']} {person['lastname']} is {person['year']}-year student in {person['faculty']}")


#task5
with open('api-result.json') as file:
    text = json.load(file)

print(f"{text['query']['pages']['13801']['title']}\n{text['query']['pages']['13801']['extract']}")

