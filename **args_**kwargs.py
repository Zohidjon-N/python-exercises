# def find_product(*numbers):
#     product=1
#     if not numbers: #false(false)=true
#         return 0
#     for number in numbers:
#         product*=number
    
#     return product


# print(find_product(1,2,3,4,5))
# print(find_product())

def info_student(name, surname, **student_info):

    student_info['name']=name
    student_info['surname']=surname

    return student_info

print(info_student('Ali', 'Ahmad', grade= 4, subject='history'))
