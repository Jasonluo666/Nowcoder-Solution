import sys

error_num = 0
error_records = {}
order = []
for line in sys.stdin:
    file_loc, error_line = line.split()

    file_name = None
    for index in range(1, len(file_loc) + 1):
        if index == 16 or index == len(file_loc) or file_loc[-index] == '\\':
            file_name = file_loc[-index + 1:]
            break
    
    error_num += 1
    if (file_name, error_line) not in error_records.keys():
        order.append((file_name, error_line))

        error_records[(file_name, error_line)] = 1
        if len(order) > 8:
            error_records[order[0]] = 0
            order = order[1:]
    else:
        error_records[(file_name, error_line)] += 1

for key in order:
    print(key[0], key[1], error_records[key])
