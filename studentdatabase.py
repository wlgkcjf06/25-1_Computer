import database as db

def main():
    while True:
        print("---------------------")
        print("1. Add Student")
        print("2. Print All Students")
        print("3. Delete Student")
        print("4. Exit")
        opt = input("Choose an option: ")
        print("---------------------")
        if opt == '1':
            id = input("Enter student ID: ")
            name = input("Enter student name: ")
            db.add_student(id,name)
        elif opt == '2':
            db.print_students()
        elif opt == '3':
            id = input("Enter student ID: ")
            db.delete_student(id)
        elif opt == '4':
            print("Exiting...")
            break

main()