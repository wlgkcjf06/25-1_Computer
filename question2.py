def find_start(line):
    """Return index of 'S'."""
    for i in range(len(line)):
        if line[i] == 'S':
            return i

def find_end(line):
    """Return index of 'E'."""
    for i in range(len(line)):
        if line[i] == 'E':
            return i

def move_position(pos, direction):
    """Return new position given 'L', 'R', or 'J'."""
    if direction == 'L':
        return pos-1
    elif direction == 'R':
        return pos+1
    elif direction == 'J':
        return pos+2

def is_valid(line, pos):
    """Return True if position is in bounds and not a wall."""
    if pos<0 or pos>len(line)-1:
        return False
    elif line[pos]==1:
        return False
    else:
        return True


def simulate_runner(line, commands):
    """
    Simulate the runner's movement.
    Print each step and the final outcome.
    """
    pos = find_start(line)
    for cm in commands:
        newpos = move_position(pos, cm)
        if is_valid(line, newpos) and (cm =='R' or cm == 'L'):
            print(f"Moved to {newpos}")
            pos = newpos
        elif is_valid(line, newpos) and (cm == 'J'):
            print(f"Jumped to {newpos}")
            pos = newpos
        else:
            print(f"Blocked at {newpos}")
    print(f"Final position: {pos}")
    if pos == find_end(line):
        print("Reached exit? Yes")
    else:
        print("Reached exit? No")



# Test cases
# Additional test(with other 'line') will be used during grading.
#################################################################
# DO NOT MODIFY THE CODE BELOW.
#################################################################
line = ["S", 0, 0, 1, 0, "E"]
short_line = [0, "S", 0, 1, "E"]
print("1. Test 'find_start', 'find_end'")
print(f"find_start(line)={find_start(line)}")
print(f"find_end(line)={find_end(line)}")
print()

print("2. Test 'move_position'")
print(f"move_position(0, 'R')={move_position(0, 'R')}")
print(f"move_position(2, 'L')={move_position(2, 'L')}")
print(f"move_position(1, 'J')={move_position(1, 'J')}")
print()

print("3. Test 'is_valid'")
print(f"is_valid(line, 0)={is_valid(line, 0)}")
print(f"is_valid(line, 2)={is_valid(line, 2)}")
print(f"is_valid(line, 3)={is_valid(line, 3)}")   #False
print(f"is_valid(line, -1)={is_valid(line, -1)}") #False
print(f"is_valid(line, 6)={is_valid(line, 6)}") #False
print(f"is_valid(line, 7)={is_valid(line, 7)}") #False
print()

print("4. Test 'simulate_line'")
simulate_runner(line, "RRLRJR")
simulate_runner(line, "RRJRR")
simulate_runner(line, "LRJRJR")
simulate_runner(line, "RRJLJ")
simulate_runner(line, "LLJL")
simulate_runner(short_line, "LJJ")