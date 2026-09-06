import pickle

filename ='pi_million_digits.txt'

with open(filename) as file:
    content = file.read().replace('\n','').replace(' ','')  
    print('05112005' in content)

with open('new_file.pkl','wb') as file:
    pickle.dump(content,file) 

with open('file.txt','a') as file:
    while True:
        text = input('Your wish(or exit):')
        if text == 'exit':
            break
   
        file.write(text,'\n')



        

