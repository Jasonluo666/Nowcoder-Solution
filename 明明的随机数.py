import sys 

for line in sys.stdin:
    input_num = int(line)

    table = [False for x in range(1000)]
    for _ in range(input_num):
        input_element = int(input())
        table[input_element] = True

    for index in range(len(table)):
        if table[index] == True:
            print(index)