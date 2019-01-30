input_num = int(input())

table = {}

for _ in range(input_num):
    line = input().split(' ')
    if int(line[0]) not in table.keys():
        table[int(line[0])] = int(line[1])
    else:
        table[int(line[0])] += int(line[1])

sorted_keys = sorted(list(table.keys()))

for key in sorted_keys:
    print(str(key) + ' ' + str(table[key]))
