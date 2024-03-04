class Student:
    def __init__(self, name, id, total, std):
        self.name = name
        self.id = id
        self.total = total
        self.std = std

    def __repr__(self):
        return f"Student(name='{self.name}', id={self.id}, total={self.total}, class={self.std})"

    @staticmethod
    def sort_students(students, sort_property):
        if all(hasattr(student, sort_property) for student in students):
            return sorted(students, key=lambda x: getattr(x, sort_property))
        else:
            print(f"Property '{sort_property}' does not exist in at least one Student object.")
            return students

# Example usage:
students = []
num_students = int(input("Enter the number of students: "))
for i in range(num_students):
    name = input("Enter student name: ")
    id = int(input("Enter student ID: "))
    total = float(input("Enter student total: "))
    std = int(input("Enter student class: "))
    students.append(Student(name, id, total, std))

property_to_sort = input("Enter property to sort by (name, id, total, std): ")
sorted_students = Student.sort_students(students, property_to_sort)
for student in sorted_students:
    print(student)
