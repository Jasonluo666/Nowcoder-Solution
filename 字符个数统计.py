input_str = input()

map = [False for x in range(127)]
count = 0
for element in input_str:
    if map[ord(element) - 1] == False:
        map[ord(element) - 1] = True
        count += 1

print(count)