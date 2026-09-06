class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.level = 1
        self.subjects = []

    def __repr__(self):
        return f"{self.name} {self.surname}" 

    def __lt__(self, other):
        return self.level < other.level
    def __eq__(self, other):
        return self.level == other.level

    def get_info(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nLevel: {self.level}\nSubjects: {self.subjects}"  

    def upgrade_level(self):
        self.level+=1    

    def take_subject(self, cls_subject):
        self.subjects.append(cls_subject)
    
    
    def remove_subject(self, name_subject):
        for subject in self.subjects:
            if subject.name == name_subject:
                self.subjects.remove(subject)
                return
        
        print('You didn\'t take this course')

class Subject:
    def __init__(self,name):
        self.name = name
        self.students =[]

    def add_student(self,student):
        if isinstance(student, Student):
            return self.students.append(student)
    def __getitem__(self, index):
        return self.students[index]

    def __setitem__(self, index, student):
        if isinstance(student, Student):
            self.students[index] = student
        
    def __len__(self):
        return len(self.students)
     




student1 = Student('Anvar','Karimov') 
student1.upgrade_level()
math = Subject('mathematics')  
student1.take_subject(math) 
student1.remove_subject('bio')    

print(student1.get_info())
print(student1==student1)



