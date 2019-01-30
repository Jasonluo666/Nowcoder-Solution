input_str = input().split(' ')

output = []
for element in input_str[::-1]:
    output.append(element)

print(' '.join(output))