def load_students(filename="courses.txt"):
    students = {}
    f = open('courses.txt', 'r')
    line = f.readline()
    while len(line) != 0:
        tmp = line.split()
        students[tmp[0]] = tmp[1:]
        line = f.readline()
    f.close()
    return students

def handle_common(students, s1, s2):
    common_courses = set()
    if s1 not in students or s2 not in students:
        print("One or both students not found.")
        return
    for course in students[s1]:
        if course in students[s2]:
            common_courses.add(course)
    print("Common courses:", ", ".join(common_courses))

def handle_union(students, s1, s2):
    union_courses = set()
    if s1 not in students or s2 not in students:
        print("One or both students not found.")
        return
    for course in students[s1]:
        union_courses.add(course)
    for course in students[s2]:
        if course not in union_courses:
            union_courses.add(course)
    print("Union courses:", ", ".join(union_courses))

def handle_all(students):
    all_courses = set()
    for value in students.values():
        for course in value:
            if course not in all_courses:
                all_courses.add(course)
    print("All courses:", ", ".join(all_courses))
def handle_unique(students, target):
    if target not in students:
        print("Student not found.")
        return
    unique = set(students[target])
    for key in students:
        if key != target:
            for course in students[key]:
                if course in unique:
                    unique.remove(course)
    print("Unique courses:", ", ".join(sorted(unique)))
def main():
    students = load_students()
    while True:
        command = input("Enter command: ").strip()
        if command == "exit":
            break
        parts = command.split()
        if not parts:
            continue

        cmd = parts[0]
        if cmd == "common" and len(parts) == 3:
            handle_common(students, parts[1], parts[2])
        elif cmd == "union" and len(parts) == 3:
            handle_union(students, parts[1], parts[2])
        elif cmd == "all":
            handle_all(students)
        elif cmd == "unique":
            handle_unique(students, parts[1])
        else:
            print("Unknown or malformed command.")
if __name__ == "__main__":
    main()