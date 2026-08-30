class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.level = 1
        self.subjects = []

    def get_info(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nLevel: {self.level}\nSubjects: {self.subjects}"  

    def upgrade_level(self):
        self.level+=1    

    def take_subject(self, cls_subject):
        self.subjects.append(cls_subject)
    
    
    def remove_subject(self, name_subject):
        if name_subject.name in self.subjects:
            self.subjects.remove(name_subject.name)
        else:
            print('You didn\'t take this course')

class Subject:
    def __init__(self,name):
        self.name = name


student1 = Student('Anvar','Karimov') 
student1.upgrade_level()
math = Subject('mathematics')  
student1.take_subject(math) 
student1.remove_subject('bio')    

print(student1.get_info())
