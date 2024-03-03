class Student:
    def __init__(self, name, id, total, class_num):
        self.name = name
        self.id = id
        self.total = total
        self.class_num = class_num

    def __repr__(self):
        return f"Student(name='{self.name}', id={self.id}, total={self.total}, class={self.class_num})"

def sort_students(students, property):
    if hasattr(Student, property):
        return sorted(students, key=lambda x: getattr(x, property))
    else:
        print(f"Property '{property}' does not exist in Student object.")
        return students

# Example usage:
students = []
num_students = int(input("Enter the number of students: "))
for i in range(num_students):
    name = input("Enter student name: ")
    id = int(input("Enter student ID: "))
    total = float(input("Enter student total: "))
    class_num = int(input("Enter student class: "))
    students.append(Student(name, id, total, class_num))

property_to_sort = input("Enter property to sort by (name, id, total, class_num): ")
sorted_students = sort_students(students, property_to_sort)
for student in sorted_students:
    print(student)



#---------------------------------------------------------------------------------------------
    

class Student:
    def __init__(self, name, id, total, class_num):
        self.name = name
        self.id = id
        self.total = total
        self.class_num = class_num

    def __repr__(self):
        return f"Student(name='{self.name}', id={self.id}, total={self.total}, class={self.class_num})"

def sort_students(students, property):
    if hasattr(Student, property):
        return sorted(students, key=lambda x: getattr(x, property))
    else:
        print(f"Property '{property}' does not exist in Student object.")
        return students

# Example usage:
students = [
    Student("Alice", 101, 95.5, 10),
    Student("Bob", 102, 85.0, 11),
    Student("Charlie", 103, 90.0, 10)
]

property_to_sort = 'total'  # Change this to any valid property like 'name', 'id', 'total', 'class_num'
sorted_students = sort_students(students, property_to_sort)
for student in sorted_students:
    print(student)


#---------------------------------------------------------------------------------------------
    
class Student:
    def __init__(self, name, id, total, class_num):
        self.name = name
        self.id = id
        self.total = total
        self.class_num = class_num

    def __repr__(self):
        return f"Student(name='{self.name}', id={self.id}, total={self.total}, class={self.class_num})"

def sort_students(students, property):
    return sorted(students, key=lambda x: getattr(x, property))

# Example usage:
students = [
    Student("Alice", 101, 95.5, 10),
    Student("Bob", 102, 85.0, 11),
    Student("Charlie", 103, 90.0, 10)
]

sorted_students = sort_students(students, 'total')
for student in sorted_students:
    print(student)
