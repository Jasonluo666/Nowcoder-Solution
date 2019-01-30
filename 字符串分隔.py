str_1 = input()
str_2 = input()

length_cons = 8

output_str = []
while len(str_1) > 0 or len(str_2) > 0:
    if len(str_1) > 0:
        if len(str_1) / length_cons >= 1:
            output_str.append(str_1[:length_cons])
            str_1 = str_1[length_cons:]
        else:
            add_zeros = ''.join(['0' for x in range(length_cons - len(str_1))])
            output_str.append(str_1 + add_zeros)
            str_1 = ''
    else:
        if len(str_2) / length_cons >= 1:
            output_str.append(str_2[:length_cons])
            str_2 = str_2[length_cons:]
        else:
            add_zeros = ''.join(['0' for x in range(length_cons - len(str_2))])
            output_str.append(str_2 + add_zeros)
            str_2 = ''
for element in output_str:
    print(element)