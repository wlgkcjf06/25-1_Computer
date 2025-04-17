_students = []

def add_student(i, n):
    _students.append([i,n])

def delete_student(id):
    for i in range(len(_students)):
        if _students[i][0] == id:
            _students.pop(i)

def print_students():
    for i in range(len(_students)):
        print(f"ID: {_students[i][0]}, Name: {_students[i][1]}")