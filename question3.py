#########################
# DO NOT EDIT THIS FILE #
#########################

from question3_module import *
from question3_utils import *

def main():
    # DO NOT EDIT THIS FUNCTION.
    input_list = [3, 4, 5]
    cursor = 1

    while True:
        print_list_and_menu(input_list, cursor)

        i = int(input("Select the number: "))

        if i == 1:
            if not is_full(input_list):
                value = int(input("Input value: "))
                input_list = append_front(input_list, value)
                cursor = move_cusor_right(input_list, cursor)
            else:
                warning()
        elif i == 2:
            if not is_full(input_list):
                value = int(input("Input value: "))
                input_list = append_back(input_list, value)
            else:
                warning()
        elif i == 3:
            if is_empty(input_list):
                warning()
            else:
                input_list = remove_front(input_list)
                if not is_empty(input_list):
                    cursor = move_cusor_left(input_list, cursor)
        elif i == 4:
            if is_empty(input_list):
                warning()
            else:
                input_list = remove_back(input_list)
                if cursor == len(input_list) and not is_empty(input_list):
                    cursor = move_cusor_left(input_list, cursor)
        elif i == 5:
            if not is_full(input_list):
                value = int(input("Input value: "))
                input_list = insert(input_list, value, cursor)
                cursor = move_cusor_right(input_list, cursor)
            else:
                warning()
        elif i == 6:
            if is_empty(input_list):
                warning()
            else:
                input_list = delete(input_list, cursor)
            if not is_empty(input_list):
                cursor = move_cusor_left(input_list, cursor)
        elif i == 7:
            if not is_empty(input_list):
                cursor = move_cusor_right(input_list, cursor)
            else:
                warning()
        elif i == 8:
            if not is_empty(input_list):
                cursor = move_cusor_left(input_list, cursor)
            else:
                warning()
        elif i == 9:
            print("Exit Program.")
            break

if __name__=="__main__":
    main()