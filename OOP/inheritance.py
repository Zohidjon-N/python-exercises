from uuid import uuid4
class Person:
    __count = 0 #private class attribute
    def __init__(self, name,surname,y_birth):
        self.name = name
        self.surname = surname
        self.y_birth = y_birth
        self.__id = uuid4() #private attribute
        Person.__count +=1

    @property
    def get_id(self):
        return self.__id

    @classmethod
    def get_count(cls):
        return cls.__count


    def get_info(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nYear of birth: {self.y_birth}"  

    def get_age(self,year):
        return year - self.y_birth  



class User(Person):
    def __init__(self,name,surname,y_birth,email):
        super().__init__(name,surname,y_birth)
        self.email = email


    def get_info(self):
        return f"{super().get_info()}\nEmail: {self.email}"  #polymorphism


user = User('Asad','Iqbolov',2005,'asad.iqbo77@gmail.com')
print(user.get_info())


class Admin(User): #Multi-level inheritance
    def __init__(self,name,surname,y_birth,email):
        super().__init__(name,surname,y_birth,email)
        self.death_note = []

    def ban_user(self, name):
        self.death_note.append(name)
        return f"Blocked: {name}"

admin = Admin('adm','ADM',2000,'nomailcom')

print(admin.ban_user('aziz'))

print(f"ID:{user.get_id}\nCount: {Person.get_count()}")
        