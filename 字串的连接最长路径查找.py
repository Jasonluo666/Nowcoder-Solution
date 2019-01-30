input_num = int(input())

output = []
for _ in range(input_num):
    input_str = input()
    output.append(input_str)

output = sorted(output)
for element in output:
    print(element)
