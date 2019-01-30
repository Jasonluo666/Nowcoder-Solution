input_num = input().split('.')

integer = int(input_num[0])
decimal = int(input_num[1][0])

if decimal >= 5:
    integer += 1

print(integer)