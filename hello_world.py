class StudentCollection:
    def __init__(self, student: "Student"):
        self.student = student

    def __iter__(self):
        return self

    def __next__(self):
        if not self.student:
            raise StopIteration
        student = self.student
        if hasattr(self.student, 'neighbor'):
            self.student = self.student.neighbor
        else:
            self.student = None
        return student


class Student:
    def __init__(self, name: str, neighbor: "Student" = None):
        self.name = name
        if neighbor:
            self.neighbor = neighbor


if __name__ == "__main__":
    student1 = Student('Petia')
    student2 = Student('Vasia', neighbor=student1)
    student3 = Student('Kolia', neighbor=student2)

    student_col = StudentCollection(student3)

    for student in student_col:
        print(student.name)


def create_slogan(name: str) -> str:
    if type(name) != str:
        print(f'name is not type of str. Type of name: {type(name)}, data: {name}')
    else:
        return f"{name} drinks pepsi in his brand new BMW"
# positive
assert create_slogan("S@SH05") == "* drinks pepsi in his brand new *"
# negative
assert create_slogan([1, [2, 3]]) == None