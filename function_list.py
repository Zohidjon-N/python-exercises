#version1
def capitalize(names):
    for i in range(len(names)):
        names[i] = names[i].title() 

    return names

names = ['ali', 'vali', 'hasan', 'husan']  
print(capitalize(names))

#version2
def capitalize_it(names):
    return [name.title() for name in names]

print(capitalize_it(names))
print(names)


