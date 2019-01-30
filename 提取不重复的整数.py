input_int = input()

table = {}
new_int = ''
for element in input_int[::-1]:
    if element not in table.keys():
        table[element] = True
        new_int += element

print(new_int)