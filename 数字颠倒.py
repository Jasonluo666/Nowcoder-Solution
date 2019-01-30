input_int = list(input())

for index in range(int(len(input_int) / 2)):
    temp = input_int[index]
    input_int[index] = input_int[-index - 1]
    input_int[-index - 1] = temp

print(''.join(input_int))