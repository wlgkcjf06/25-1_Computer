FILENAME = "grades.txt"
def load_from_file():
    data = []
    try:
        f = open(FILENAME, 'r')
        line = f.readline().strip()
        while line != '':
            data.append(line.split(','))
            line = f.readline().strip()
        f.close()
    except IOError:
        print(f"⚠ File '{FILENAME}' not found. Starting with empty database.")
    return data

def save_to_file(data):
    w = open(FILENAME, 'w')
    for l in data:
        nl = [str(k) for k in l]
        line = ','.join(nl)
        line = line + '\n'
        w.write(line)
    w.close()

def calculate_average(kor, eng, math):
    avg_score = format((kor+eng+math) / 3, '.1f')
    return avg_score

def add_student(data):
    name = input("Name: ").strip()
    student_id = input("Student ID: ").strip()
    kor = int(input("Korean score: "))
    eng = int(input("English score: "))
    math = int(input("Math score: "))
    avg = calculate_average(kor, eng, math)
    data.append([name,student_id,kor,eng,math,avg])
    print("✅ Student added.")

def delete_student(data):
    student_id = input("Enter student ID to delete: ").strip()
    found = False
    for i in range(len(data)):
        if data[i][1] == student_id:
            data.pop(i)
            found = True
    if not found:
        print("⚠ No student with that ID found.")

def search_student(data):
    keyword = input("Enter name or ID to search: ").strip()
    found = False
    for i in range(len(data)):
        if data[i][0]==keyword or data[i][1]==keyword:
            found = True
            print_student(data[i])
    if not found:
        print("❌ No matching student found.")

def print_student(student):
    print("\n📇 Student Info")
    print(f"Name : {student[0]}")
    print(f"Student ID: {student[1]}")
    print(f"Korean : {student[2]}")
    print(f"English : {student[3]}")
    print(f"Math : {student[4]}")
    print(f"Average : {student[5]}")

def list_students(data):
    if not data:
        print("📭 No student data.")
        return
    print("\n📋 All Students:")
    print("{:<10} {:<8} {:>6} {:>6} {:>6} {:>8}".format("Name", "ID", "Kor", "Eng", "Math", "Average"))
    print("-" * 50)
    for student in data:
        print("{:<10} {:<8} {:>6} {:>6} {:>6} {:>8}".format(
        student[0], student[1], student[2], student[3], student[4], student[5]
    ))

def main():
    data = load_from_file()
    print("Welcome to Grade Management System")
    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Search Student")
        print("4. List All Students")
        print("5. Save & Exit")
        choice = input("Choose (1-5): ").strip()
        if choice == "1":
            add_student(data)
        elif choice == "2":
            delete_student(data)
        elif choice == "3":
            search_student(data)
        elif choice == "4":
            list_students(data)
        elif choice == "5":
            save_to_file(data)
            print("💾 Data saved. Goodbye!")
            break
        else:
            print("⚠ Invalid option. Try again.")

if __name__ == "__main__":
    main()