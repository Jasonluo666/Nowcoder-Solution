import sys

for line in sys.stdin:
    orders = line.split(';')

    current_pos = [0, 0]
    for order in orders:
        if (len(order) == 2 or len(order) == 3) and (order[0] == 'A' or order[0] == 'D' or order[0] == 'W' or order[0] == 'S'):
            direction = order[0]
            step = order[1:]

            if step.isdigit():
                step = int(step)

                if direction == 'A':
                    current_pos[0] -= step
                elif direction == 'D':
                    current_pos[0] += step
                elif direction == 'W':
                    current_pos[1] += step
                elif direction == 'S':
                    current_pos[1] -= step

    print(str(current_pos[0]) + ',' + str(current_pos[1]))
