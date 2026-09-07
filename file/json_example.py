import json

data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}

json_data = json.dumps(data)
print(json_data)
print(type(json_data))


talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}""" 

talaba = json.loads(talaba_json)
print(f"{talaba['ism']} {talaba['familiya']}") 


with open('data.json','w') as file:
    json.dump(json_data, file)

with open('talaba.json','w') as file:
    json.dump(talaba_json,file)



    