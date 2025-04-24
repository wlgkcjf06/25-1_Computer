binary_list = []
while True:
    val = input("Enter 0 or 1 (any other key to stop): ") 
    if val != '0' and val != '1':
        break
    binary_list.append(int(val))

max_count = 0
cntr = 0

for i in binary_list:
    if i == 1:
        cntr += 1
    elif i == 0:
        cntr = 0
    if max_count < cntr:
        max_count = cntr

print(max_count)
