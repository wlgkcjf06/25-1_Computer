#########################
# DO NOT EDIT THIS FILE #
#########################

def warning():
    # DO NOT EDIT THIS FUNCTION.
    print()
    print("[Warning] Invalid command!")

def print_list_and_menu(input_list, cursor):
    # DO NOT EDIT THIS FUNCTION.
    print()
    print("Current List")
    if len(input_list) != 0:
        for i in input_list:
            print(f"|{i}", end="")
        print("|")
    else:
        print("| |")
    print(" ", end="")
    for space in range(cursor):
        print(" " * 2, end="")
    print("*")

    print("1: Append front")
    print("2: Append back")
    print("3: Remove front")
    print("4: Remove back")
    print("5: Insert")
    print("6: Delete")
    print("7: Move cusor right")
    print("8: Move cusor left")
    print("9: Exit program")